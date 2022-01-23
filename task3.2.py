# task3.2
from hw4.Convert import convert
money_str = input("Введите число для перевода: ")
print("Ты ввёл", money_str, "рублей")
# проверка на пустое значение
if money_str == '':
    print("Вы ввели пустое поле. Введите число")
# проверка на число
else:
    try:
        money_int = int(money_str)
        # проверка, что число положительное
        if money_int < 0:
            print("Введите положительное число")
        else:
            print("Конвертированная сумма в USD = ", convert(money_int)[0])
            print("Конвертированная сумма в EUR = ", convert(money_int)[1])
            print("Конвертированная сумма в CHF = ", convert(money_int)[2])
            print("Конвертированная сумма в GBP = ", convert(money_int)[3])
            print("Конвертированная сумма в CNY = ", convert(money_int)[4])
    except ValueError:
        print("Вы ввели не число. Введите число")
