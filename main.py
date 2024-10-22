class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар {item_name} добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удалён.")
        else:
            print(f"Товар {item_name} не найден.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товара нет, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена на {new_price}.")
        else:
            print(f"Товар {item_name} не найден.")

# Создаем три магазина с разными названиями и адресами
store1 = Store("Магазин Продукты", "ул. Ленина, 1")
store2 = Store("Товары для дома", "ул. Советская, 10")
store3 = Store("Электроника", "пр. Победы, 45")

# Добавляем товары в каждый магазин
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("soap", 1.5)
store2.add_item("shampoo", 4.2)

store3.add_item("laptop", 1200)
store3.add_item("smartphone", 800)

# Тестируем методы магазина store1

# Добавляем новый товар
store1.add_item("oranges", 0.65)

# Обновляем цену существующего товара
store1.update_price("bananas", 0.80)

# Удаляем товар
store1.remove_item("apples")

# Запрашиваем цену товара
price = store1.get_price("bananas")
if price is not None:
    print(f"Цена на bananas: {price}")
else:
    print("Товар bananas не найден.")

# Пытаемся запросить цену несуществующего товара
price = store1.get_price("grapes")
if price is not None:
    print(f"Цена на grapes: {price}")
else:
    print("Товар grapes не найден.")
