print("It is working!")


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print([factorial(s) for s in z])
