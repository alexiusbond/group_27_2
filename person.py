class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Name: {self.__name} age: {self.__age}'


if __name__ == '__main__':
    student = Person('Aivar', 20)
    print(student)
