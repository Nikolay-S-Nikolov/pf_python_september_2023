data = input().split()
store_data = {}
for i in range(0, len(data), 2):
    product = data[i]
    quantities = data[i + 1]
    store_data[product] = int(quantities)

product_to_search = input().split()

for product in product_to_search:
    if product in store_data:
        print(f"We have {store_data.get(product)} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
