class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        # Основное строковое представление базового класса
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return self.__str__()


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        # Строковое представление для бумажной книги
        return f"Книга: {self.name}. Автор: {self.author}, страниц: {self.pages}"

    def __repr__(self):
        return self.__str__()


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # длительность в часах (или другой единице)

    def __str__(self):
        # Строковое представление для аудиокниги
        return f"Аудиокнига: {self.name}. Автор: {self.author}, длительность: {self.duration} ч"

    def __repr__(self):
        return self.__str__()


# Пример использования
if __name__ == "__main__":
    b = Book("Базовый класс книг", "Автор Неизвестен")
    p = PaperBook("Пример бумаги", "Автор Паперы", 320)
    a = AudioBook("Слушай и учись", "С.А. Автор", 5.75)

    print(b)
    print(p)
    print(a)