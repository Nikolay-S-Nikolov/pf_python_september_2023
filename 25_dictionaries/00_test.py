my_dict = {1: 'apple', 2: 'banana'}
my_dict.clear()  # Remove all items from my_dict
print(my_dict)

my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()  # a shallow copy of my_dict
print(my_dict == copied_dict)

my_dict = {"fruit": "apple", "vegetable": "cucumber"}
apple = my_dict.pop("fruit")  # pop an item by key
print(my_dict)

my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict.popitem())  # remove the last item in my_dict
print(my_dict)

students = {"name": "George", "course": "Fundamentals"}
del students["course"]  # removes an item by key name
print(students)

students = {"name": "George", "course": "Fundamentals"}
del students  # the dictionary completely
# print(students)  # NameError

my_dict = {"fruit": "apple", "vegetable": "cucumber"}
superfood = my_dict.setdefault("superfood", "bean")
# Insert key with a value of default if key is not in the dictionary
print(my_dict)

my_dict = {"fruit": "apple", "vegetable": "cucumber"}
superfood_dict = {"superfood": "bean"}
my_dict.update(superfood_dict)  # dict.update inserts the superfood_dict in the end of my_dict
print(my_dict)  # {'fruit': 'apple', 'vegetable': 'cucumber', 'superfood': 'bean'}

students = {
    1: {'name': 'Peter', 'age': 22},
    2: {'name': 'Alex', 'age': 21}
}
first_student_name = students[1]['name']
print(first_student_name)  # Peter
students[3] = {}  # {3: {}}
students[3]['name'] = 'Amy'  # {3: {'name': 'Amy'}}
students[3]['age'] = 25  # {3: {'name': 'Amy', 'age': 25}}
print(students)

students = {
    1: {'name': 'Peter', 'age': 22},
    2: {'name': 'Alex', 'age': 21},
    3: {'name': 'Amy', 'age': 25}
}
print()

for v, k in students.items():
    print(f"*** Student: {v} ***")
    for data, value in k.items():
        print(data, ": ", value)
    print()
