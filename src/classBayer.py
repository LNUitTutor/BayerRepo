# Клас, що моделює товар, має назву, ціну за одиницю, кількість
class Article:
    def __init__(self, n, p, c):
        self.name = n
        self.price = p
        self.count = c
    def __str__(self):
        return f"Товар({self.name}:{self.price}x{self.count})"
    def salePrice(self):
        return self.price * self.count

a = Article('Молоко', 20.95, 2)
print(a)
print(a.salePrice())
