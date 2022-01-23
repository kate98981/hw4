# task4.2
import sys


def convert(money, item):
    ryb_to_usd = 0.013039
    ryb_to_eur = 0.011507
    ryb_to_chf = 0.011922
    ryb_to_gbp = 0.009615
    ryb_to_cny = 0.082664
    if item == 'USD':
        return int(money * ryb_to_usd)
    elif item == 'EUR':
        return int(money * ryb_to_eur)
    elif item == 'CHF':
        return int(money * ryb_to_chf)
    elif item == 'GBP':
        return int(money * ryb_to_gbp)
    elif item == 'CNY':
        return int(money * ryb_to_cny)


try:
    while True:
        items = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
        item_string = "['USD', 'EUR', 'CHF', 'GBP', 'CNY']"
        currency_item = input("Выберите один из 5 вариантов " + item_string + ":")
        for i in range(len(items)):
            if items[i] == currency_item:
                money_str = input("Введите число для перевода: ")
                print("Вы ввели сумму", money_str, "и валюту", items[i])
                if money_str == '':
                    print("Вы ввели пустое поле. Введите число")
                else:
                    try:
                        ryb = int(money_str)
                        # проверка, что число положительное
                        if ryb < 0:
                            print("Введите положительное число")
                        else:
                            result = convert(ryb, items[i])
                            print("Конвертированная сумма в", items[i], result)
                    except ValueError:
                        print("Вы ввели не число. Введите число")
                break
            elif i == len(items) - 1:
                print("Введенная валюта не найдена")
except KeyboardInterrupt:
    sys.exit()
