name = 'Yevhen'                                #тип даних str(рядок)
age = 15                                    #тип даних int(ціле число)
height = 1.72                               #тип даних float(з комою)
is_student = True                           #тип даних bool(так, ні)
hobbies = ['dance', 'books']                #тип даних list(з змінами)
friends = {"Artem", "Vlad"}                  #тип даних set(множина)
birthday = (3, 10, 2009)                    #тип даних tuple(без змін)
book =  {'aftg': 'allforthegame'}           #тип даних dict (бібліотека)

print('name', type(name),':', name)           #type-повертає тип змінної
print('age', type(age),':', age)
print('height', type(height),':', height)
print('is_student', type(is_student),':', is_student)
print('hobbies', type(hobbies),':', hobbies)
print('friends', type(friends),':', friends)
print('birthday', type(birthday),':', birthday)
print('book', type(book),':', book)

a = 52
b = 8

c = a + b                #додавання
print(c)

d = a - b                #віднімання
print(d)

n = a * b                 #множення
print(n)

f = a / b                 #діленння (результат завжди float)
print(f)

g = a // b                #ділення без остачі
print(g)

s = a % b                 #остача від ділення
print(s)

x = a ** b                #піднесення до степення
print(x)
