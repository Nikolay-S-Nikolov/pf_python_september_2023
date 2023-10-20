qty_food = float(input())
qty_hay = float(input())
qty_cover = float(input())
weight = float(input())

for day in range(1, 31):
    qty_food -= 0.3
    if day % 2 == 0:
        qty_hay -= qty_food * 0.05
    if day % 3 == 0:
        qty_cover -= weight / 3
    if qty_food < 0 or qty_hay < 0 or qty_cover < 0:
        break

if float(f'{qty_food:.2f}') <= 0 or float(f"{qty_hay:.2f}") <= 0 or float(f"{qty_cover:.2f}") <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {qty_food:.2f}, Hay: {qty_hay:.2f}, Cover: {qty_cover:.2f}.")
