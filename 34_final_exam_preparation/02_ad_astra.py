import re

text_string = input()

pattern = r"([#|])([A-Za-z ]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d\d?\d?\d?)(\1)"
result = re.findall(pattern, text_string)
total_calories = sum(int(x[5]) for x in result)
days_with_food = total_calories//2000
print(f"You have food to last you for: {days_with_food} days!")

for item in result:
    print(f"Item: {item[1]}, Best before: {item[3]}, Nutrition: {item[5]}")
