"""
    Крок четвертий. Виконаємо виявлення майбутніх днів народження. Зараз наша мета, це навчитися порівнювати дати.
    На цьому кроці ми будемо використовувати раніше реалізовані нами функції:

string_to_date - перетворює рядок у дату
date_to_string - перетворює дату у рядок
prepare_user_list - створює список користувачів з датою народження яка записана в форматі datetime

    Вам необхідно реалізувати перший варіант функції get_upcoming_birthdays, яка приймає список користувачів з другого кроку і визначає, 
чи настає їх день народження для користувачів з цього списку протягом наступних N днів. На другому кроці ми створювали такий список за допомоги функції prepare_user_list.
    Вивід функції get_upcoming_birthdays — це список користувачів, чиї дні народження настають протягом наступних заданих N днів. 
Кожен елемент списку словник, що містить два ключі: name і congratulation_date. Ключ name вказує на ім'я особи, чий день народження наближається. 
Ключ congratulation_date містить дату, коли слід привітати цю особу, також у форматі рядка, згідно з форматом рік.місяць.день (наприклад, "2024.03.30").
    Отже, виконання функції get_upcoming_birthdays має виконуватися так:

users = [
    {"name": "Sarah Lee", "birthday": "1957.03.30"},
    {"name": "John Doe", "birthday": "1985.03.28"},
    {"name": "Jane Smith", "birthday": "1990.03.27"},
    {"name": "John Doe", "birthday": "1985.01.23"},
]

print(get_upcoming_birthdays(prepare_user_list(users, 7)))

    Якщо ми виконали код 27.03.2024, то в виведенні ми повинні отримати список користувачів для яких настає їх день народження в наступні 7 днів.

[
    {"name": "Sarah Lee", "congratulation_date": "2024.03.30"},
    {"name": "John Doe", "congratulation_date": "2024.03.28"},
    {"name": "Jane Smith", "congratulation_date": "2024.03.27"},
]

    Що виглядає цілком логічно. Для реалізації цього завдання вам потрібно дописати код функції get_upcoming_birthdays:

from datetime import datetime, date

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    # Тут повинна бути реалізована основна логіка

    return upcoming_birthdays

    Зверніть увагу, що поточну дату ми отримуємо саме через today = date.today(). Це необхідно, щоб перевірка могла упевнитись, 
що ваша функція працює як потрібно. Тому не потрібно змінювати це на datetime.today().date(), це дасть такий же результат виконання, 
але перевірка не зможе перевірити роботу вашої функції.
    Також вже створено список upcoming_birthdays, яка зберігатиме ім'я користувача та відповідну дату привітання, 
якщо день народження відбувається протягом наступних days днів.
"""

from datetime import datetime, date

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if 0 <= (birthday_this_year - today).days <= days:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(birthday_this_year)}) 
    return upcoming_birthdays

users = [
    {"name": "Sarah Lee", "birthday": "1957.04.30"},
    {"name": "John Doe", "birthday": "1985.04.20"},
    {"name": "Jane Smith", "birthday": "1990.04.21"},
    {"name": "John Doe", "birthday": "1985.04.23"},
]

print(get_upcoming_birthdays(prepare_user_list(users), 7))