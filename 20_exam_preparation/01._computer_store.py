TAXES = 0.20
DISCOUNT = 0.10

command = input()
total_price = 0

while command != "special" and command != "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price
    command = input()

if total_price == 0:
    print("Invalid order!")

else:
    taxes = total_price * TAXES
    price_with_taxes = total_price + taxes
    if command == "special":
        price_with_taxes -= price_with_taxes * DISCOUNT
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")
