def apply_discount(price, percent=20):
    discount = price * percent / 100
    final_price = price - discount

    print("Original Price:", price)
    print("Discount:", percent, "%")
    print("Final Price:", final_price)


apply_discount(1000)

apply_discount(1000, percent=30)