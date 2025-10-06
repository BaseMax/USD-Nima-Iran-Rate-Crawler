import re
import requests
import time
import csv

def clean_html(text):
    """Remove HTML tags from a string"""
    return re.sub(r'<.*?>', '', text)

base_url = (
    "https://api.tgju.org/v1/market/indicator/summary-table-data/nima_buy_usd?"
    "lang=fa&order_dir=asc&draw=9&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D="
    "&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true"
    "&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true"
    "&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true"
    "&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true"
    "&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true"
    "&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true"
    "&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true"
    "&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false"
    "&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true"
    "&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D="
    "&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false"
    "&start={start}&length=30&search=&order_col=&order_dir=&from=1369%2F07%2F01&to=1404%2F07%2F15&convert_to_ad=1&_="
)

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8,it;q=0.7",
    "cache-control": "no-cache",
    "origin": "https://www.tgju.org",
    "pragma": "no-cache",
    "referer": "https://www.tgju.org/",
    "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

start = 0
length = 30
all_rows = []

while True:
    url = base_url.format(start=start)
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error {response.status_code} at start={start}")
        break
    
    data = response.json()
    
    if not data.get("data"):
        print("No more data, stopping...")
        break
    
    print(f"Start={start}, Number of rows={len(data['data'])}")
    
    for row in data["data"]:
        cleaned_row = [clean_html(item) for item in row]
        all_rows.append(cleaned_row)
    
    start += length
    time.sleep(1)

csv_file = "tgju_nima_buy_usd.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Open", "Close", "High", "Low", "Price", "Change%", "Date_Gregorian", "Date_Persian"])
    writer.writerows(all_rows)

print(f"All data saved to {csv_file}")
