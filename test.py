import current_rates

rates = current_rates.rates_list()
currency_code = [i[1] for i in rates]
#print(currency_code)

code = "GBP"

match = [i[3] for i in rates if i[1] == code][0]
print(match)

result = f'{(round(1.3456 * 100000, 2)):.2f}'

print (result)