import re

pattern = r"%([A-Z][a-z]+)%[^|$%.]*<([A-Za-z0-9_]+)>[^|$%.]*\|(\d+)[^|$%.]*\|[^|$%.]*?(\d+\.?\d+?)\$"
income = 0
while True:
    input_line = input()
    if input_line == "end of shift":
        break
    result = list(re.findall(pattern, input_line))
    if result:
        customer_name, product, count, price = result[0]
        total_price = int(count) * float(price)
        print(f"{customer_name}: {product} - {total_price:.2f}")
        income += total_price
print(f"Total income: {income:.2f}")
