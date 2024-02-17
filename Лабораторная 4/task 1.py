class Big_city:
    """Базовый класс большой горож.

    :param name: Название города.
    :param population: Население города.
    :param region: Регион города.
    Все атрибуты имею защиту от вмешательства для изменения, так как некоторые
    атрибуты не могут быть изменены.
    """

    def __init__(self, name: str, population: int, region: str):
        self._name = name
        self._population = population
        self._region = region

    def __str__(self):
        return f"Город {self._name} расположен в {self._region} и имеет население {self._population}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._region!r}, {self._population!r})"

    def division_population(self, divider: int) -> int:
        """Функция для разделения населения.

        :param divider: Делитель.
        :return: Разделенное население на указанный делитель
        """
        return self._population // divider

    @property
    def name(self) -> str:
        """Возвращение имени города.
        :return: Имя города
        """
        return self._name

    @property
    def population(self) -> int:
        """Возвращение населения города.
        :return: Населения города
        """
        return self._population

    @property
    def region(self) -> str:
        """Возвращение региона города.
        :return: Региона города
        """
        return self._region

    @population.setter
    def population(self, new_population: int) -> None:
        """Функция изменения населения города.

        :raise: TypeError, если new_population тип не соответствует int
        :raise: ValueError, если население меньше 1
        :param new_population: Новая численность населения.
        """
        if not isinstance(new_population, int):
            raise TypeError("Тип не соответствует")
        if new_population <= 0:
            raise ValueError("Количество меньше 1")
        self._population = new_population


class Small_city(Big_city):
    """Базовый класс большой горож.

    :param name: Название города.
    :param population: Население города.
    :param region: Регион города.
    :param dependent_city: Город, от которого идет зависимость.
    Все атрибуты имею защиту от вмешательства для изменения, так как некоторые
    атрибуты не могут быть изменены.
    """

    def __init__(self, name: str, population: int, region: str, dependent_city: str):
        super().__init__(name, population, region)
        self._dependent_city = dependent_city

    def __str__(self):
        return f"Город {self._name} расположен в {self._region}, имеет население {self._population} " \
               f"и зависим от {self._dependent_city}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._region!r}, {self._population!r}, {self._dependent_city!r})"

    def division_population(self, divider: int) -> int:
        """Функция для разделения населения.

        :param divider: Делитель.
        :return: Разделенное население на указанный делитель
        """
        return self._population // divider

    @property
    def dependent_city(self) -> str:
        """Возвращает город, от которого идет зависимость.
        :return: Город, от которого идет зависимость
        """
        return self._dependent_city

    @dependent_city.setter
    def dependent_city(self, new_dependent_city: str) -> None:
        """Функция изменения зависимости от города.

        :raise: TypeError, если new_dependent_city тип не соответствует str
        :raise: ValueError, если new_dependent_city является пустой строкой
        :param new_dependent_city: Новый город, от которого идет зависимость.
        """
        if not isinstance(new_dependent_city, str):
            raise TypeError("Тип не соответствует")
        if new_dependent_city == "":
            raise ValueError("Название не может быть пустым")
        self._dependent_city = new_dependent_city


if __name__ == "__main__":
    city1 = Big_city("St. Peterburg", 5600004, "Lenengradskay")
    print(city1)
    print(city1.name)
    print(city1.__repr__())
    city1.population = city1.population + 1
    print(city1)
    print(city1.division_population(2))
    city2 = Small_city("Viborg", 37309, "Lenengradskay", "St. Peterburg")
    print(city2)
    print(city2.name)
    print(city2.__repr__())
    city2.population = city2.population + 1
    print(city2)
    city2.dependent_city = "Moscow"
    print(city2)
    print(city2.division_population(2))
    pass
