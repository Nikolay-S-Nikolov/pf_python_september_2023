# print("It is working!")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width


rect = Rectangle(4, 5)
result = rect.calculate_area()
print(result)

rect.resize(6, 7)
result = rect.calculate_area()
print(result)
