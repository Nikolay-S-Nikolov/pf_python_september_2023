import re

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)"
bought_furniture = []
total_cost = 0
while True:
    purchase = input()
    if purchase == "Purchase":
        break
    result = re.findall(pattern, purchase)
    # print(result)
    if result:
        bought_furniture.append(result[0][0])
        total_cost += float(result[0][1])*int(result[0][2])

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
