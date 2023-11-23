product_price_dict = {}
product_qty_dict = {}
command = input()

while command != "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in product_price_dict:
        product_price_dict[product] = price
        product_qty_dict[product] = 0
    product_qty_dict[product] += quantity
    if product_price_dict[product] != price:
        product_price_dict[product] = price
    command = input()

for name in product_price_dict.keys():
    total_price = product_price_dict[name] * product_qty_dict[name]
    print(f"{name} -> {total_price:.2f}")
