# sehw2output.py
# 讀取 expenses.csv，依類別(category)加總金額並畫出圓餅圖

import csv
import os
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


def load_category_sum():
    """讀取 expenses.csv，回傳 {category: 總金額} 的字典"""
    if not os.path.exists(FILE_NAME):
        print("❌ 找不到 expenses.csv，請先執行輸入程式記一兩筆資料。")
        return {}

    category_sum = defaultdict(float)

    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_cols = {"amount", "category"}
        if not required_cols.issubset(reader.fieldnames or []):
            print("❌ expenses.csv 欄位格式不正確，至少要有 amount, category。")
            return {}

        for row in reader:
            amount_str = row.get("amount", "").strip()
            category = row.get("category", "").strip()

            if category == "":
                category = "others"

            try:
                amount = float(amount_str)
            except ValueError:
                continue

            if amount <= 0:
                continue

            category_sum[category] += amount

    return category_sum


def plot_pie(category_sum):
    """接收 {category: 總金額}，畫出圓餅圖並存成 sample_pie.png"""
    if not category_sum:
        print("📭 沒有有效的支出資料，無法畫圖。")
        return

    labels = list(category_sum.keys())
    sizes = list(category_sum.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("expense distribution by category")
    plt.axis("equal")

    output_file = "sample_pie.png"
    plt.savefig(output_file, bbox_inches="tight")
    print(f"✅ 圓餅圖已儲存為 {output_file}")
    plt.show()


def main():
    data = load_category_sum()
    plot_pie(data)


if __name__ == "__main__":
    main()
