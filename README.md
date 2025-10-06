# USD-Iran-Rate-Crawler

A Python crawler to fetch historical **Nima Buy USD rates** from TGJU (Tehran Stock Exchange) and save them as a CSV file. 

This repository contains a **Python crawler and scraper** for fetching historical **Nima Buy USD rates** from TGJU (Tehran Stock Exchange). It automatically collects data from the TGJU API and saves it as a CSV file.

## Features

- Scrapes USD to Iranian Rial Nima Buy rates from TGJU.
- Cleans HTML tags from the API response.
- Iterates through all available historical data automatically.
- Saves the complete dataset in UTF-8 CSV format.
- Columns include: `Open`, `Close`, `High`, `Low`, `Price`, `Change%`, `Date_Gregorian`, `Date_Persian`.
- Automatically iterates through all available data using TGJU API.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/BaseMax/USD-Iran-Rate-Crawler.git
cd USD-Iran-Rate-Crawler
````

2. Run the crawler:

```bash
python crawler.py
```

3. The output CSV file `tgju_nima_buy_usd.csv` will be generated in the same directory.

## Requirements

* Python 3.x
* `requests` library

Install dependencies:

```bash
pip install requests
```

## License

This project is licensed under the MIT License.

Copyright 2025, Max Base
