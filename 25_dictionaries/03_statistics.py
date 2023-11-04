line = input()
stock = {}
while line != "statistics":
    product, quantity = line.split(": ")
    quantity = int(quantity)
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity
    line = input()
print("Products in stock:")
for k, v in stock.items():
    print(f"- {k}: {v}")
count_all_products = len(stock)
sum_all_quantities = sum(stock.values())
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
