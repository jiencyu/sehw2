# expense_input.py
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# ---------------------------------------------------
# 初始化：如果檔案不存在，建一個並寫入欄位名稱
# ---------------------------------------------------
def ensure_file_with_header():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "notes"])

# ---------------------------------------------------
# 各種輸入驗證
# ---------------------------------------------------
def input_date(prompt="請輸入日期 (YYYY-MM-DD)："):
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ 日期格式錯誤，請重新輸入！")

def input_amount():
    while True:
        amount_str = input("請輸入金額：")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("❌ 金額必須大於 0！")
                continue
            return amount
        except ValueError:
            print("❌ 金額必須是數字，請重新輸入！")

def input_category():
    category = input("請輸入類別 (food/transport/entertainment/others)：")
    if category.strip() == "":
        category = "others"
    return category

def input_notes():
    return input("請輸入備註（可空白）：")

# ---------------------------------------------------
# 功能 1：新增支出
# ---------------------------------------------------
def add_expense():
    print("\n--- 新增支出 ---")
    date = input_date()
    amount = input_amount()
    category = input_category()
    notes = input_notes()

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, notes])

    print("✅ 已新增支出！")

# ---------------------------------------------------
# 功能 2：顯示已輸入幾筆資料
# ---------------------------------------------------
def count_expenses():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as f:
            rows = list(csv.reader(f))
            count = len(rows) - 1  # 減掉 header
            print(f"\n📊 目前已輸入 {count} 筆資料。\n")
    except FileNotFoundError:
        print("\n📁 找不到資料檔案。\n")

# ---------------------------------------------------
# 功能 3：查詢某天的支出
# ---------------------------------------------------
def search_by_date():
    print("\n--- 查詢某天支出 ---")
    target = input_date("請輸入想查詢的日期 (YYYY-MM-DD)：")

    found = []
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"] == target:
                found.append(row)

    if len(found) == 0:
        print("📭 該日期沒有支出紀錄。\n")
    else:
        print(f"\n📅 {target} 的支出如下：")
        for item in found:
            print(f"- NT$ {item['amount']} ({item['category']}), 備註：{item['notes']}")
        print()

# ---------------------------------------------------
# 主選單
# ---------------------------------------------------
def main():
    ensure_file_with_header()

    while True:
        print("\n====== 簡易記帳系統 ======")
        print("1. 新增項目")
        print("2. 查看目前已輸入幾筆")
        print("3. 查詢某天記帳情形")
        print("4. 離開")
        print("==========================")

        choice = input("請選擇功能 (1-4)：")

        if choice == "1":
            add_expense()
        elif choice == "2":
            count_expenses()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            print("👋 已離開程式。")
            break
        else:
            print("❌ 選項無效，請重新輸入！")

if __name__ == "__main__":
    main()
