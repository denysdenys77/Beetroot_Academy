# Написать класс-регистратор для существующих классов. В классе должна быть переменная класса _registry, в которую
# необходимо добавить ссылку на класс обернутый декоратором. Реализовать метод get_registry для того чтоб посмотреть
# какие классы были зарегестрированы.


class ClassRegistrar:

    _registry = []

    @classmethod
    def wrapper(cls, other):
        ClassRegistrar._registry.append(other)

    @staticmethod
    def get_registry():
        for x in ClassRegistrar._registry:
            x = f'Registered Class at: {x}'
            print(x)


@ClassRegistrar.wrapper
class Person:
    pass

@ClassRegistrar.wrapper
class Student:
    pass

@ClassRegistrar.wrapper
class Teacher:
    pass


ClassRegistrar.get_registry()
