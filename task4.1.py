# task4.1
import sys

ryb_to_usd = 0.013039
ryb_to_eur = 0.011507
ryb_to_chf = 0.011922
ryb_to_gbp = 0.009615
ryb_to_cny = 0.082664

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
                            convert = 0
                            if items[i] == 'USD':
                                convert = int(ryb * ryb_to_usd)
                            elif items[i] == 'EUR':
                                convert = int(ryb * ryb_to_eur)
                            elif items[i] == 'CHF':
                                convert = int(ryb * ryb_to_chf)
                            elif items[i] == 'GBP':
                                convert = int(ryb * ryb_to_gbp)
                            elif items[i] == 'CNY':
                                convert = int(ryb * ryb_to_cny)
                            print(convert)
                    except ValueError:
                        print("Вы ввели не число. Введите число")
                break
            elif i == len(items) - 1:
                print("Введенная валюта не найдена")
        print("meow2")
except KeyboardInterrupt:
    sys.exit()
