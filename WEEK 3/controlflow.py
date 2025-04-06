def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
       price = price - (price * discount_percent / 100)
       return price
    else:
        return price

price = int(input("Enter price of item "))
discount_percent = int(input("Enter discount percentage "))
print(calculate_discount(price,discount_percent))