# task3.1
ryb_to_usd = 0.013039
ryb_to_eur = 0.011507
ryb_to_chf = 0.011922
ryb_to_gbp = 0.009615
ryb_to_cny = 0.082664
money_str = input("Введите число для перевода: ")

# проверка на пустое значение
if money_str == '':
    print("Вы ввели пустое поле. Введите число")

# проверка на число
else:
    try:
        ryb = int(money_str)
        # проверка, что число положительное
        if ryb < 0:
            print("Введите положительное число")
        else:
            convert_to_usd = int(ryb * ryb_to_usd)
            convert_to_eur = int(ryb * ryb_to_eur)
            convert_to_chf = int(ryb * ryb_to_chf)
            convert_to_gbp = int(ryb * ryb_to_gbp)
            convert_to_cny = int(ryb * ryb_to_cny)
            currency_item = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
            convert_all = [convert_to_usd, convert_to_eur, convert_to_chf, convert_to_gbp, convert_to_cny]
            for i in range(len(currency_item)):
                print("Конвертированная сумма в", currency_item[i], convert_all[i])
    except ValueError:
        print("Вы ввели не число. Введите число")
