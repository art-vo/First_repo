"""
    Пригадаємо як звучить наше завдання. У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, 
вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. 
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
    У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Цей список виглядає наступним чином.
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
    Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, 
якщо це необхідно.
    Ми виконали майже все і нам залишилось виконати останні кроки:
    Дописати функцію get_upcoming_birthdays. Ми повинні додати в функцію використання написаної нами на попередньому кроці функцію adjust_for_weekend. 
Врахувати перенесення дати на наступний робочий день, якщо день народження припадає на вихідний.
Також потрібно врахувати, що день народження вже може відбутися наступного року. Наприклад ми запускаємо функцію 30 грудня, і напевно є можливість, 
що день народження відбудеться вже наступного року в перших числах січня. Отже, перевірте, чи вже минув день народження в цьому році if birthday_this_year < today. 
Якщо так, розгляньте дату на наступний рік.
    Важливо! Збережіть цю домашню роботу. Вам знадобиться в наступних домашніх завданнях, для інших модулів навчання, використання функції get_upcoming_birthdays.
"""
from datetime import datetime, date, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        #end_of_year = datetime(year=today.year, month=12, day=31)
        if birthday_this_year < today: 
            birthday_this_year = user["birthday"].replace(year=today.year + 1)
        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(users, days=7))