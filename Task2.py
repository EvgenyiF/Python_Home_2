# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Задача не понятна от слова совсем нет ни формулы ни примера

summ = 0
n = int ( input ( 'Введите число: ' ))
# myDict = {i: round((1+1/i)**i,2) for i in range(1,n+1)}
for i in range(1,n+1):
    summ += (1+1/i)**i
# print(f' Список чисел последовательности: {myDict}')
print(f' Сумма последовательности (1+1/i)**i равна {round(summ,2)}')