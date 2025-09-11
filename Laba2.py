list = [5, 8, 'apple', 2, 'dog', 11, 'banana', 4, 'zoo', 10, 1, 'cat', 6, 'orange', 3, 'grape', 12, 'kiwi', 9, 'mango']

ints = []
strs = []

for x in list:
    if isinstance(x, int):
        ints.append(x)
    elif isinstance(x, str):
        strs.append(x)

ints.sort()
strs.sort()

main_sorted = ints + strs
even_ints = [x for x in ints if x % 2 == 0]
strs_caps = [s.upper() for s in strs]

print("Відсортований список:", main_sorted)
print("Список кратних 2:", even_ints)
print("Список рядків у капсі:", strs_caps)
