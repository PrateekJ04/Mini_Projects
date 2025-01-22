# This project ensures end to end purchase flow from kirana store vendor


products = []
prices = []
quantities = []
# vocal interatcion friendly communication
total_price = []
print("Kaise ho bhai kya chahiye tha?")
while True:
    product = input("Batao Kya chahiye: ")
    price = float(input(f"ye {product} ka bhi batata hu aapko: "))
    quantity = float(input("Abhi kitna chahiye: "))
    if product and price and quantity is not None:
        products.append(product)
        prices.append(price)
        quantities.append(quantity)
        ask = input("Aur kuch chahiye(ha/nahi): ")
        if ask.lower() == "nahi":
            break

print(f"\nBhaiya aapka pura saaman ye raha")
for i in products:
    print(i, end=', ')

d1 = dict(zip(prices, quantities))
for key, value in d1.items():
    total_price.append(key * value)

total = sum(total_price)

print(f"\nYe pura saaman aapka {total} rupay ka hua")
ask_for_payment = input(f"\nAap isko payTM kardo ya cash dedo dono chalega(hogaya/nahi hua): ")

if ask_for_payment.lower() == "hogaya":
    print("Aapka bohot bohot dhanyawad, firse jarur aayiyega, Aapka din shubh ho")
else:
    req = input("Kar do bhai dhandha manda hai ye time: ")
    if req.lower() == "ha" or "hogaya":
        print("Thik hai")
