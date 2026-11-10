
class ShoppingCart:
    def __init__(self):
        self.products = ["Shoes", "Watch", "Bag", "Headphones"]

    def __len__(self):
        return len(self.products)

    def __getitem__(self, position):
        return self.products[position]


cart = ShoppingCart()

print("Total Products:", len(cart))

print("Product 1:", cart[0])
print("Product 2:", cart[1])
print("Product 3:", cart[2])
