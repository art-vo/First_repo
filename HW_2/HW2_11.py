"""Напишіть функцію format_string, яка центрує рядок у рамках заданої довжини length.

Задачі:

Створіть функцію format_string, яка приймає два аргументи: string рядок, який потрібно форматувати та length довжина, у межах якої потрібно центрувати рядок.
Якщо довжина string більша або дорівнює length, поверніть рядок без змін.
Якщо довжина string менша за length, додайте перед рядком пробіли, для того, щоб рядок був центрований у рамках length. Кількість пробілів визначте за формулою (length - len(string)) // 2.
Поверніть з функції відформатований рядок, що центрується у межах length.
Очікуваний результат:

Функція format_string повертає відформатований рядок відповідно до заданих правил.

Підказки:

Використовуйте len() для визначення довжини рядка.
Для створення рядка з пробілів використовуйте " " * кількість_пробілів."""

string = input("Enter your string:\n")
length = int(input("Enter your length:\n"))

def format_string(string, length) -> str:
    if len(string) >= length:
        return string
    else:
        half_gep_length = (length - len(string)) // 2 
        half_gep = " " * half_gep_length
        return f"{half_gep}{string}"

print(format_string(string, length))