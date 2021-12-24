# EC2 Spot Price Fetcher
> A small CLI for fetching spot price of EC2 instances across multiple regions.

## Installation

### 1. Install dependencies
```bash
make install
```

### 2. Run the application
```bash
python fetch_prices.py --instance-type <INSTANCETYPE>

# e.g.:

python fetch_prices.py --instance-type c6i.xlarge
```
