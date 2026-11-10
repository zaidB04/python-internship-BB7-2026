def process_order(order):

    try:
        item = order["item"]
        price = order["price"]

    except KeyError:
        print("Error: Required order details are missing!")

    else:
        print("Item:", item)
        print("Price:", price)

    finally:
        print("Processing complete")


order1 = {"item": "Mobile", "price": 30000}

order2 = {"item": "Tv"}

process_order(order1)

print()

process_order(order2)