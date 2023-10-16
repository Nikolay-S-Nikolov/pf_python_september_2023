TOP_COUNT = 5
numbers = [int(x) for x in input().split()]
avg_num = sum(numbers) / len(numbers)
filtered_numbers = sorted([num for num in numbers if num > avg_num])
if filtered_numbers:
    # for i in range(TOP_COUNT):
    #     if filtered_numbers:
    #         print(filtered_numbers.pop(), end=" ")
    print(*[filtered_numbers.pop() for i in range(TOP_COUNT) if filtered_numbers])
else:
    print("No")
