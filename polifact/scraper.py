import requests
from bs4 import BeautifulSoup
import re
import argparse
import csv
import os
from stats import category_stats, time_stats, data_quality

# 定义基础 URL 和正则表达式
BASE_URL = "https://www.politifact.com/factchecks/list/"
date_pattern = re.compile(r"\w+ \d{1,2}, \d{4}")

# 抓取多页数据
def scrape_category(category, speaker):
    page = 1
    results = []
    while True:
        url = f"{BASE_URL}?category=&ruling={category}&speaker={speaker}&page={page}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        statements = soup.find_all("li", class_="o-listicle__item")

        if not statements:  # 没有更多内容
            break

        for statement in statements:
            # 提取标题
            quote_wrap = statement.find("div", class_="m-statement__quote-wrap")
            title = quote_wrap.get_text(strip=True) if quote_wrap else "No Title"

            # 提取日期
            desc = statement.find("div", class_="m-statement__desc")
            date_match = date_pattern.search(desc.text if desc else "")
            date = date_match.group() if date_match else "No Date"

            # 提取链接
            link_tag = quote_wrap.find("a", href=True) if quote_wrap else None
            link = f"https://www.politifact.com{link_tag['href']}" if link_tag else "No Link"

            # 保存结果
            results.append({"category": category, "title": title, "date": date, "link": link})

        page += 1
    return results

# 保存为 CSV
def save_to_csv(results, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 确保路径存在
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["category", "title", "date", "link"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {file_path}")

# 主函数，处理命令行参数
def main():
    parser = argparse.ArgumentParser(description="Scrape PolitiFact data.")
    parser.add_argument("-s", "--speaker", type=str, required=True, help="Name of the speaker (e.g., joe-biden)")
    parser.add_argument("-c", "--category", type=str, default="all", help="Category to scrape (e.g., mostly-true, half-true, etc.)")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output CSV file path (e.g., ./results.csv)")
    args = parser.parse_args()

    # 定义类别
    categories = ["mostly-true", "half-true", "barely-true", "false", "pants-fire"]
    results = []

    if args.category == "all":
        # 如果类别为 "all"，抓取所有类别
        for cat in categories:
            results.extend(scrape_category(cat, args.speaker))
    elif args.category in categories:
        # 指定具体类别
        results = scrape_category(args.category, args.speaker)
    else:
        print("Invalid category. Please choose from: all, mostly-true, half-true, barely-true, false, pants-fire.")
        return

    # 保存为 CSV
    save_to_csv(results, args.output)
    results = scrape_category("all", "joe-biden")  # 调用抓取函数
    category_stats(results)
    time_stats(results)
    data_quality(results)

