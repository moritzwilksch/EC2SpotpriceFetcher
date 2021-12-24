# 💵 EC2 Spot Price Fetcher <img width=40px src=https://user-images.githubusercontent.com/58488209/147372034-79219d4d-78ba-4bd5-a71d-08d74372fa5e.png>  
> A small CLI for fetching spot price of EC2 instances across multiple regions.


## ⌨️ Usage
```bash
python fetch_prices.py --instance-type <INSTANCETYPE>
```
<img width=600px src=https://user-images.githubusercontent.com/58488209/147371984-ee4f528b-290c-4925-a9ce-816576fe559e.gif>


## ⚒️ Installation

### 1. Install dependencies
```bash
make install
```

### 2. Configure boto3 credentials
Use the AWS CLI
```bash
aws configure
```

... or ...

Create credentials file manually
```bash
# ~/.aws/credentials
[default]
aws_access_key_id = XXXXXX
aws_secret_access_key = XXXXXXXXXXXX
```

### 3. Run the application
```bash
python fetch_prices.py --instance-type <INSTANCETYPE>

# e.g.:

python fetch_prices.py --instance-type c6i.xlarge
```
