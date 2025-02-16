# Задано послідовність пар чисел вигляду ціна:кількість
#  що закінчується нулем.
# Обчислити (суму заданих чисел) загальну ціну - сума добутків.

def inputPair():
    answer = input("Введіть пару 'ціна:кількість': ").split(":")
    return float(answer[0]), (int(answer[1]) if len(answer)>1 else 1)
    
def inputAndSum():
# Підготовка
    summa = 0.0
    price, count = inputPair()

# Основний цикл
    while price > 0:
        summa += price * count
        price, count = inputPair()
# Повернення результату
    return summa

# Обслуговуємо трьох покупців
s = 0.0
for i in range(3):
    b = inputAndSum()
    s += b
    print(f"bayer({i+1}) : {b}")
# Виведення результату
print("Total =", s)
