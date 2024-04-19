"""
На першому кроці ми виконаємо роботу з датами. Мета кроку це ознайомлення з базовими операціями над датами які нам знадобляться для цієї задачі.
Напишіть функцію string_to_date, яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date.
Напишіть зворотну функцію date_to_string, яка приймає об'єкт datetime.date і повертає рядкове представлення дати в форматі "YYYY.MM.DD".
Ці функції повинні працювати наступним чином:

        date_string = "2024.01.01"
        converted_date = string_to_date(date_string)
        print(converted_date)
        date_string = date_to_string(converted_date)
        print(date_string)
        Виконання такого коду призведе до наступного виведення:

        2024-01-01
        2024.01.01 

"""

from datetime import datetime

date_string = "2024.01.01"

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

converted_date = string_to_date(date_string)
print(converted_date)


def date_to_string(converted_date):
    return datetime.strftime(converted_date, "%Y.%m.%d")

date_string = date_to_string(converted_date)
print(date_string)

    