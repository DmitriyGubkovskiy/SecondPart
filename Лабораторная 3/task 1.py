class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.set_pages(pages)

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._author!r}, {self._pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Тип не соответствует")
        if new_pages <= 0:
            raise ValueError("Количсетсво страниц меньше 1")
        self._pages = new_pages

    def set_pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Тип не соответствует")
        if new_pages <= 0:
            raise ValueError("Количсетсво страниц меньше 1")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.set_duration(duration)

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._author!r}, {self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Тип не соответствует")
        if new_duration <= 0:
            raise ValueError("Продолжительность меньше 1")
        self._duration = new_duration

    def set_duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Тип не соответствует")
        if new_duration <= 0:
            raise ValueError("Продолжительность меньше 1")
        self._duration = new_duration


book1 = Book("AAA", "BBB")
print(book1)
print(book1.__repr__())
print(book1.name)
book2 = PaperBook("EAR", "WEF", 120)
print(book2)
print(book2.__repr__())
print(book2.name)
book3 = AudioBook("FCD", "OVE", 215.3)
print(book3)
print(book3.__repr__())
print(book3.name)
