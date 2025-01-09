# stats.py
from collections import Counter
from datetime import datetime

def category_stats(results):
    categories = [item["category"] for item in results]
    count = Counter(categories)
    print("Category Statistics:")
    for category, num in count.items():
        print(f"  {category}: {num}")
    print()

def time_stats(results):
    dates = [datetime.strptime(item["date"], "%B %d, %Y") for item in results if item["date"] != "No Date"]
    years = [date.year for date in dates]
    year_count = Counter(years)
    print("Yearly Statistics:")
    for year, num in year_count.items():
        print(f"  {year}: {num}")
    print()

def data_quality(results):
    empty_titles = [item for item in results if item["title"] == "No Title"]
    broken_links = [item for item in results if item["link"] == "No Link"]
    print("Data Quality Report:")
    print(f"  Empty Titles: {len(empty_titles)}")
    print(f"  Broken Links: {len(broken_links)}")
    print()
