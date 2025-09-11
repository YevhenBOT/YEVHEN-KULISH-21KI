# Створюємо список з 10 int та 10 str елементів
main_list = [42, 15, 7, 88, 23, 56, 31, 4, 99, 18, 
            "яблуко", "банан", "вишня", "дата", "ескімо", 
            "фінік", "гітара", "зима", "кіт", "літо"]

print("Оригінальний список:")
print(main_list)
print()

# Сортуємо список: спочатку int по зростанню, потім str від а до я
int_elements = [x for x in main_list if isinstance(x, int)]
str_elements = [x for x in main_list if isinstance(x, str)]

sorted_int = sorted(int_elements)
sorted_str = sorted(str_elements)

sorted_list = sorted_int + sorted_str

print("Відсортований список (int по зростанню, потім str від а до я):")
print(sorted_list)
print()

# Знаходимо елементи кратні двом (тільки для int)
even_elements = [x for x in main_list if isinstance(x, int) and x % 2 == 0]

print("Елементи кратні двом:")
print(even_elements)
print()

# Створюємо список з str елементів у верхньому регістрі
uppercase_str = [x.upper() for x in main_list if isinstance(x, str)]

print("Строкові елементи у верхньому регістрі:")
print(uppercase_str)
print()

# Виводимо всі списки з підписами
print("=" * 50)
print("РЕЗУЛЬТАТИ:")
print("=" * 50)
print("1. Оригінальний список:")
print(f"   {main_list}")
print()
print("2. Відсортований список (int ↑, str а→я):")
print(f"   {sorted_list}")
print()
print("3. Елементи кратні двом:")
print(f"   {even_elements}")
print()
print("4. Строкові елементи у верхньому регістрі:")
print(f"   {uppercase_str}")