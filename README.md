# EC2 Spot Price Fetcher
> A small CLI for fetching spot price of EC2 instances across multiple regions.


## Usage
```
python fetch_prices.py --instance-type <INSTANCETYPE>
```
<img width=600px src=https://user-images.githubusercontent.com/58488209/147371984-ee4f528b-290c-4925-a9ce-816576fe559e.gif>


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
