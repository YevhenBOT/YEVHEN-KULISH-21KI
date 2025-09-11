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

# Виводимо всі змінні з їх типами через type()
print("age:", age, f"({type(age).__name__})")
print("height:", height, f"({type(height).__name__})")
print("name:", name, f"({type(name).__name__})")
print("is_student:", is_student, f"({type(is_student).__name__})")
print("hobbies:", hobbies, f"({type(hobbies).__name__})")
print("grades:", grades, f"({type(grades).__name__})")
print("person:", person, f"({type(person).__name__})")
print("unique_numbers:", unique_numbers, f"({type(unique_numbers).__name__})")
print("none_value:", none_value, f"({type(none_value).__name__})")

# Арифметичні оператори
x, y = 10, 3
print("x + y =", x + y, f"({type(x + y).__name__})")
print("x - y =", x - y, f"({type(x - y).__name__})")
print("x * y =", x * y, f"({type(x * y).__name__})")
print("x / y =", x / y, f"({type(x / y).__name__})")
print("x // y =", x // y, f"({type(x // y).__name__})")
print("x % y =", x % y, f"({type(x % y).__name__})")
print("x ** y =", x ** y, f"({type(x ** y).__name__})")

# Логічні оператори
a, b = True, False
print("a and b =", a and b, f"({type(a and b).__name__})")
print("a or b =", a or b, f"({type(a or b).__name__})")
print("not a =", not a, f"({type(not a).__name__})")
