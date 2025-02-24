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
    def __add__(self, article):
        if self.name == article.name:
            return Article(self.name, min(self.price, article.price), self.count + article.count)
        else:
            return none
    def __iadd__(self, article):
        if self.name == article.name:
            self.price = min(self.price, article.price)
            self.count += article.count
        return self
    def __lt__(self, other):
        return self.salePrice() < other.salePrice()

a = Article('Молоко', 20.95, 3)
b = Article('Молоко', 22.25, 2)
print(a, b)
print(a.salePrice())
c = a + b
print(c)
c += b
print(c)
if a < b:
    print("a =", a)
else:
    print("b =", b)
