inventory = {
    "mobile": 10,
    "charger": 20,
    "headphone": 15
}

# Add new stock
def add_stock(product, quantity):

    inventory[product] = inventory.get(product, 0) + quantity

    print(quantity, product, "added successfully")


# Sell product
def sell_product(product, quantity):

    if product not in inventory:

        print(product, "does not exist!")

    elif inventory[product] >= quantity:

        inventory[product] -= quantity

        print(quantity, product, "sold successfully")

    else:

        print("Insufficient stock!")


# Testing
add_stock("Mobile", 10)

add_stock("Charger", 5)

sell_product("headphone", 2)

sell_product("laptop", 1)

sell_product("Keyboard", 20)

print("\nFinal Inventory:")
print(inventory)