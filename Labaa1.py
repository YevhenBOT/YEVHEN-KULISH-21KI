# Змінні всіх основних типів
age = 15                      # int
height = 1.70                 # float
name = "Yevhen"               # str
is_student = True             # bool
hobbies = ["dota 2", "rust", "cs sourse"]   # list
grades = (12, 11, 10)         # tuple
person = {"name": "Yevhen", "age": 15}  # dict
unique_numbers = {1, 2, 3}    # set
none_value = None             # NoneType

# Виводимо всі змінні з їх типами (словами)
print("age:", age, "(int)")
print("height:", height, "(float)")
print("name:", name, "(str)")
print("is_student:", is_student, "(bool)")
print("hobbies:", hobbies, "(list)")
print("grades:", grades, "(tuple)")
print("person:", person, "(dict)")
print("unique_numbers:", unique_numbers, "(set)")
print("none_value:", none_value, "(NoneType)")

# Арифметичні оператори
x, y = 10, 3
print("x + y =", x + y, "(int)")
print("x - y =", x - y, "(int)")
print("x * y =", x * y, "(int)")
print("x / y =", x / y, "(float)")
print("x // y =", x // y, "(int)")
print("x % y =", x % y, "(int)")
print("x ** y =", x ** y, "(int)")

# Логічні оператори
a, b = True, False
print("a and b =", a and b, "(bool)")
print("a or b =", a or b, "(bool)")
print("not a =", not a, "(bool)")
