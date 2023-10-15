number_list = [num for num in input().split(', ')]
positive_list = [positive for positive in number_list if int(positive) >= 0]
negative_list = [negative for negative in number_list if int(negative) < 0]
even_list = [even for even in number_list if int(even) % 2 == 0]
odd_list = [odd for odd in number_list if int(odd) % 2 != 0]
print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")

