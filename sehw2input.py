# expense_input.py
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def ensure_file_with_header():
    """如果檔案不存在，就建立並寫入標頭"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "notes"])

def input_date():
    while True:
        date_str = input("請輸入日期 (YYYY-MM-DD)：")
        try:
            # 確認格式正確
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
    # 你可以自己設計固定類別或讓使用者自由輸入
    category = input("請輸入類別 (例如：food/transport/entertainment)：")
    if category.strip() == "":
        category = "others"
    return category

def input_notes():
    notes = input("請輸入備註（可空白）：")
    return notes

def add_expense():
    """輸入一筆支出並寫入 CSV 檔"""
    date = input_date()
    amount = input_amount()
    category = input_category()
    notes = input_notes()

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, notes])

    print("✅ 已新增支出！")

def main():
    print("=== 簡易記帳輸入工具 ===")
    ensure_file_with_header()

    while True:
        add_expense()
        cont = input("還要再輸入一筆嗎？(y/n)：").lower()
        if cont != "y":
            print("✅ 輸入完成，已將資料儲存至", FILE_NAME)
            break

if __name__ == "__main__":
    main()
