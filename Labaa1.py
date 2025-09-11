# Змінні всіх основних типів
age = 15                      # int — ціле число, створюємо змінну "вік"
height = 1.70                 # float — число з плаваючою крапкою, створюємо змінну "зріст"
name = "Yevhen"               # str — рядок (string), створюємо змінну "ім’я"
is_student = True             # bool — булеве значення (True або False), створюємо змінну "чи студент"
hobbies = ["dota 2", "rust", "cs sourse"]   # list — список, створюємо список хобі
grades = (12, 11, 10)         # tuple — кортеж, створюємо кортеж оцінок
person = {"name": "Yevhen", "age": 15}  # dict — словник, створюємо словник з даними
unique_numbers = {1, 2, 3}    # set — множина, створюємо множину унікальних чисел
none_value = None             # NoneType — значення "нічого", створюємо змінну без значення

# Виводимо всі змінні
print("age", age)             # int
print("height", height)       # float
print("name", name)           # str
print("is_student", is_student)  # bool
print("hobbies", hobbies)     # list
print("grades", grades)       # tuple
print("person", person)       # dict
print("unique_numbers", unique_numbers)   # set
print("none_value", none_value)           # NoneType

# Арифметичні оператори
x, y = 10, 3                  # int — створюємо змінні x=10, y=3
print(f"x + y = {x + y}")     # додавання
print(f"x - y = {x - y}")     # віднімання
print(f"x * y = {x * y}")     # множення
print(f"x / y = {x / y}")     # звичайне ділення (float)
print(f"x // y = {x // y}")   # цілочисельне ділення (int)
print(f"x % y = {x % y}")     # залишок від ділення
print(f"x ** y = {x ** y}")   # піднесення до степеня

# Логічні оператори
a, b = True, False            # bool — створюємо змінні a=True, b=False
print(f"a and b : {a and b}") # логічне "і"
print(f"a or b : {a or b}")   # логічне "або"
print(f"not a : {not a}")     # логічне "не"
