def parsePair(string):
    answer = string.strip().split(":")
    return float(answer[0]), (int(answer[1]) if len(answer)>1 else 1)

def inputList():
    data = input("Введіть покупки у форматі 'ціна:кількість, ціна:кількість, ...': ")
    return list(map(parsePair, data.split(',')))

def calcSumAndMax(purchases):
    summa = sum(price * count for price, count in purchases)
    maximum = max(map(lambda p: p[0] * p[1], purchases))
    return summa, maximum

s = 0.0
max_all = 0.0
for i in range(3):
    purchases = inputList()
    total_price, max_item_price = calcSumAndMax(purchases)
    s += total_price
    max_all = max(max_all, max_item_price)
    print(f"Покупець({i+1}): загальна сума = {total_price}, найдорожчий товар = {max_item_price}")

print("Загальна сума всіх покупок =", s)
print("Найдорожчий товар серед усіх покупців =", max_all)
