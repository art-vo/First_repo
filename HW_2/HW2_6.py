"""
Напишіть програму на Python, яка розраховує розмір кожного пакета SMS в кампанії маркетингу, уникаючи помилки поділу на нуль.

Задачі:

Ви маєте змінну pool, яка дорівнює 1000 - кількість SMS, доступних для відправлення.
Запросіть у співробітника маркетингу ввести кількість розсилок quantity.
Обчисліть розмір пакета SMS для кожної розсилки, змінна chunk, поділивши pool на quantity.
Використайте блок try-except для обробки можливої помилки ZeroDivisionError, яка може виникнути, якщо quantity буде дорівнювати 0.
Якщо виникає помилка ZeroDivisionError, виведіть повідомлення про неможливість поділу на нуль.
Очікуваний результат:

Програма має вираховувати розмір пакету SMS для розсилки, або виводити повідомлення про помилку при спробі поділу на нуль.

Підказки:

У блоку try розмістіть код, який може викликати помилку.
У блоку except вкажіть тип помилки, яку ви очікуєте, та дії, які слід виконати у випадку її виникнення.
"""
#--------------------------------------------------------------------------------------------------------
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
    print(f'chunk - {chunk}')
except ZeroDivisionError:
    print('Divide by zero completed!')