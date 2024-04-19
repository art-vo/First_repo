"""
На п'ятому кроці ми виконаємо обробку вихідних днів.

Вам потрібно написати функцію adjust_for_weekend, яка приймає як аргумент дату народження birthday і перевіряє, 
чи припадає ця дата на вихідний (суботу або неділю). Якщо дата народження припадає на вихідний, 
функція знаходить наступний понеділок і повертає його як нову дату святкування. Інакше, якщо дата народження випадає на будній день, 
функція повертає оригінальну дату народження.
"""
from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        birthday = find_next_weekday(birthday, 0)
    return birthday