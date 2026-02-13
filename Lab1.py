class Humanity:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # приватна змінна (інкапсуляція)

    # геттер
    def get_age(self):
        return self.__age

    # сеттер
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Вік не може бути від'ємним")

    def introduce(self):
        print(f"Мене звати {self.name}, мені {self.__age} років.")


class Student(Humanity):
    def __init__(self, name, age, university):
        super().__init__(name, age)  # виклик конструктора батьківського класу
        self.university = university

    # поліморфізм — перевизначення методу
    def introduce(self):
        print(f"Я студент. Мене звати {self.name}, навчаюсь у {self.university}.")


human = Humanity("Євген", 16)
human.introduce()

student = Student("Женя", 16, "ТФК ЛНТУ")
student.introduce()
