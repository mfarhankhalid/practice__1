class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items)


i = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        name, qty, price = line.strip().split(",")

        try:
            qty = int(qty)
            price = int(price)
            i.add_item(name, qty, price)
        except ValueError:
            print(f"Skipping {name}: bad number")

print(f"{len(i)} items, total value {i.total_value()}")

i.remove_item("pen")
print(f"{len(i)} items, total value {i.total_value()}")

try:
    i.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")