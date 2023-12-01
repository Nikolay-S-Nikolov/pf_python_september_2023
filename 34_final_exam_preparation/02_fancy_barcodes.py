import re

count_barcode = int(input())

pattern = r"@[#]+[A-Z]{1}[A-Za-z0-9]{3}[A-Za-z0-9]+[A-Z]{1}@[#]+"

            @#{1,}[A-Z][A-Za-z0-9]{4,}[A-z]@#{1,}
pattern_group = r'\d+'

for _ in range(count_barcode):
    barcode = input()
    valid_code = re.findall(pattern, barcode)

    if valid_code:
        product_group = re.findall(pattern_group, barcode)
        if not product_group:
            x = '00'
        else:
            x = ""
            for i in product_group:
                x += i
        print(f"Product group: {x}")
    else:
        print("Invalid barcode")
