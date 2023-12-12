# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Cat:
    def __init__(self, name: str, color: str, age: int):
        """
        Создание и подготовка к работе объекта "Котик"

        :param name: Имя котика
        :param color: Цвет котика
        :param age: Возраст котика
        Примеры:
        >>> cat = Cat("Begemot", "black", 5)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет должнен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должнен иметь тип int")
        if age < 0:
            raise ValueError("Возраст не может былть отрицательным")

        self.name = name
        self.color = color
        self.age = age

    def rename(self, name: str):
        """
       Изменение имени котика
       :param name: Новое имя

       :raise TypeError: Если тип параметра не соответствует типу str
       Примеры:
       >>> cat = Cat("Begemot", "black", 5)
       >>> cat.rename("Barsik")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        self.name = name

    def get_name(self) -> str:
        """
        Возврат имени котика

        :return Имя котика

        >>> cat = Cat("Begemot", "black", 5)
        >>> cat.get_name()
        'Begemot'
        """
        return self.name

    def get_age(self) -> int:
        """
        Возврат имени котика

        :return Возраст котика

        >>> cat = Cat("Begemot", "black", 5)
        >>> cat.get_age()
        5
        """
        return self.age


class Dog:
    def __init__(self, name: str, color: str, age: int):
        """
        Создание и подготовка к работе объекта "Собачка"

        :param name: Имя Собачки
        :param color: Цвет Собачки
        :param age: Возраст Собачки
        Примеры:
        >>> dog = Dog("Sharik", "white", 7)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет должнен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должнен иметь тип int")
        if age < 0:
            raise ValueError("Возраст не может былть отрицательным")

        self.name = name
        self.color = color
        self.age = age

    def rename(self, name: str):
        """
       Изменение имени Собачки
       :param name: Новое имя Собачки

       :raise TypeError: Если тип параметра не соответствует типу str
       Примеры:
       >>> dog = Dog("Sharik", "white", 7)
       >>> dog.rename("Bobick")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        self.name = name

    def get_name(self) -> str:
        """
        Возврат имени Собачки

        :return Имя Собачки

        >>> dog = Dog("Sharik", "white", 7)
        >>> dog.get_name()
        'Sharik'
        """
        return self.name

    def get_age(self) -> int:
        """
        Возврат имени Собачки

        :return Возраст Собачки

        >>> dog = Dog("Sharik", "white", 7)
        >>> dog.get_age()
        7
        """
        return self.age


class Parrot:
    def __init__(self, name: str, color: str, age: int):
        """
        Создание и подготовка к работе объекта "Попугай"

        :param name: Имя попугая
        :param color: Цвет попугая
        :param age: Возраст попугая
        Примеры:
        >>> parrot = Parrot("Kesha", "blue", 1)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет должнен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должнен иметь тип int")
        if age < 0:
            raise ValueError("Возраст не может былть отрицательным")

        self.name = name
        self.color = color
        self.age = age

    def rename(self, name: str):
        """
       Изменение имени попугая
       :param name: Новое имя попугая

       :raise TypeError: Если тип параметра не соответствует типу str
       Примеры:
       >>> parrot = Parrot("Kesha", "blue", 1)
       >>> parrot.rename("Victor")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        self.name = name

    def get_name(self) -> str:
        """
        Возврат имени попугая

        :return Имя попугая

        >>> parrot = Parrot("Kesha", "blue", 1)
        >>> parrot.get_name()
        'Kesha'
        """
        return self.name

    def get_age(self) -> int:
        """
        Возврат имени попугая

        :return Возраст попугая

        >>> parrot = Parrot("Kesha", "blue", 1)
        >>> parrot.get_age()
        1
        """
        return self.age


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    cat = Cat("Boss", "black and white", 3)
    dog = Dog("Jack", "brown", 5)
    parrot = Parrot("Philip", "red", 2)
    doctest.testmod()
