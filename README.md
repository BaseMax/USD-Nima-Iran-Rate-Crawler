# USD-Iran-Rate-Dataset

A historical dataset of USD to Iranian Rial rates collected from TGJU (Tehran Stock Exchange). This dataset contains **Nima Buy USD rates** from 1397 to 1404 (Persian calendar).

## Dataset

- File: `tgju_nima_buy_usd-1397-1404.csv`
- Columns:
  1. `Open` – Opening rate
  2. `Close` – Closing rate
  3. `High` – Highest rate of the day
  4. `Low` – Lowest rate of the day
  5. `Price` – Price in IRR
  6. `Change%` – Daily change percentage
  7. `Date_Gregorian` – Date in Gregorian calendar
  8. `Date_Persian` – Date in Persian calendar

## Usage

You can load this CSV into Python using pandas:

```python
import pandas as pd

df = pd.read_csv("tgju_nima_buy_usd-1397-1404.csv")
print(df.head())
````

## License

This project is licensed under the MIT License.

````

---

### **2️⃣ USD-Iran-Rate-Crawler**

```markdown
# USD-Iran-Rate-Crawler

A Python crawler to fetch historical **Nima Buy USD rates** from TGJU (Tehran Stock Exchange) and save them as a CSV file. 

## Features

- Automatically iterates through all available data using TGJU API.
- Cleans HTML tags from the response.
- Saves the complete dataset in UTF-8 CSV format.
- Columns include: `Open`, `Close`, `High`, `Low`, `Price`, `Change%`, `Date_Gregorian`, `Date_Persian`.

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
