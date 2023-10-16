days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
total_plunder = 0
for day in range(1, days + 1):
    if day % 3 == 0:
        total_plunder += 1.5 * daily_plunder
    else:
        total_plunder += daily_plunder
    if day % 5 == 0:
        total_plunder = total_plunder * 0.70
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
