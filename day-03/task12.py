subscribers = {
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com",
    "d@gmail.com"
}

customers = {
    "e@gmail.com",
    "f@gmail.com",
    "g@gmail.com",
    "i@gmail.com"
}

not_purchased = subscribers - customers

not_subscribed = customers - subscribers

print("Subscribers who never purchased:", not_purchased)

print("Customers who never subscribed:", not_subscribed)