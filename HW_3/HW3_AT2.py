"""
    На другому кроці ми виконаємо операції над списками користувачів. 
Мета кроку це навчитися працювати зі списками та словниками в Python в межах нашого завдання.
    Напишіть функцію prepare_user_list, яка приймає список імен користувачів та їх дат народження у рядковому форматі, 
і повертає список словників у форматі {"name": <name>, "birthday": <birthday>}, де <birthday> - це об'єкт datetime.date.

Виконання наступного коду для вашої функції:
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

prepared_users = prepare_user_list(users)
print(prepared_users)

    Повинно призводити до виведення:
[
    {"name": "Bill Gates", "birthday": datetime.date(1955, 3, 25)},
    {"name": "Steve Jobs", "birthday": datetime.date(1955, 3, 21)},
    {"name": "Jinny Lee", "birthday": datetime.date(1956, 3, 22)},
    {"name": "John Doe", "birthday": datetime.date(1985, 1, 23)},
    {"name": "Jane Smith", "birthday": datetime.date(1990, 1, 27)},
]

Як бачимо, після виконання функції, в словнику значення ключа "birthday" має бути об'єктом datetime.date. 
Для перетворення рядка в об'єкт datetime.date використовуйте написану на першому кроці функцію string_to_date, 
яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date.
"""

from datetime import datetime

users = [                                                                                           # список користувачів
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def prepare_user_list(user_data):
    prepared_list = []                                                                              # створюємо новий список
    for user in user_data:                                                                          # заходимо в кожний елемент списку
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})  # методом .append додаємо нові рядки у список
    return prepared_list                                                                            # передаємо новий список на "вихід" функції

prepared_users = prepare_user_list(users)
print(prepared_users)