import botocore
import click
import rich
from rich.progress import track
from rich.console import Console
import boto3
import datetime
import time
import logging
from rich.status import Status

logging.basicConfig(level=logging.ERROR)

c = Console()

REGION_CONSIDERATION_SET = [
    "ca-central-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-north-1",
    "eu-south-1",
]


def get_statistics_from_results(results: list[tuple[str, str]]) -> dict:
    prices = [float(price) for _, price in results]
    n_AZs = len(results)
    if n_AZs == 0:
        return {
            "n_az": "NA",
            "min_price": "NA",
            "max_price": "NA",
            "mean_price": "NA",
            "std_price": "NA",
        }
    mean_price = sum(prices) / n_AZs
    std_price = sum([(price - mean_price) ** 2 for price in prices]) / n_AZs
    min_price = min(prices)
    max_price = max(prices)

    return {
        "n_az": n_AZs,
        "min_price": min_price,
        "max_price": max_price,
        "mean_price": mean_price,
        "std_price": std_price,
    }


def _rank(price: str) -> int:
    """ Ranks sting prices including NA """
    try:
        return float(price)
    except:
        return 1e9


@click.command()
@click.option("--instance-type", help="Specify instance type", default="t2.micro")
def fetch_prices(instance_type: str):
    table = rich.table.Table(title=f"{instance_type} prices", show_lines=False)
    table_rows = []

    table.add_column("Region", justify="left", style="cyan", no_wrap=True)
    table.add_column("Number of AZs", justify="center", style="cyan")
    table.add_column("Min Price", justify="center", style="green")
    table.add_column("Max Price", justify="center", style="red")
    table.add_column("Mean Price", justify="center")
    table.add_column("Std Price", justify="center")

    with Status(status="Fetching regions...") as status:
        for region in REGION_CONSIDERATION_SET:
            status.update(f"{region:<15}")
            client = boto3.client("ec2", region_name=region)
            results = []

            try:
                prices = client.describe_spot_price_history(
                    InstanceTypes=[instance_type],
                    ProductDescriptions=["Linux/UNIX", "Linux/UNIX (Amazon VPC)"],
                    StartTime=datetime.datetime.now().isoformat(),
                )
            except botocore.exceptions.ClientError as e:
                logging.warning(f"Boto client error for region {region}")
                continue

            for price in prices["SpotPriceHistory"]:
                results.append((price["AvailabilityZone"], price["SpotPrice"]))

            stats = get_statistics_from_results(results)
            table_rows.append(
                (
                    region,
                    *[
                        str(round(float(stat), 3)) if stat != "NA" else "NA"
                        for stat in stats.values()
                    ],
                )
            )

            c.print(f"{' DONE.':>10}", style="green")
            time.sleep(0.25)

    table_rows = sorted(table_rows, key=lambda x: _rank(x[2]))
    for row in table_rows:
        table.add_row(*row)
    c.print(table)


if __name__ == "__main__":
    fetch_prices()

