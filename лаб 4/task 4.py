import doctest

class Animal:
    """Базовый класс для всех животных."""
    def init(self, type: str, name: str, age: int) -> None:

        """Конструктор класса Животное."""
        self.type = type
        self.name = name
        self.age = age

    def str(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.type} по имени {self.name}, возраст: {self.age}"

    def repr(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Животное('{self.type}', '{self.name}', {self.age})"

    def make_sound(self) -> str:
        """Общий метод для издания звука."""
        return "Звук животного"

    def get_info(self) -> str:
        """Возвращает информацию о животном."""
        return f"Это {self.type}."


class Gorilla(Animal):
    """Дочерний класс для горилл."""

    def init(self, name: str, age: int, breed: str) -> None:
        """Конструктор класса горилла, расширяет конструктор базового класса."""
        super().init("Кошка", name, age)
        self.breed = breed

    def str(self) -> str:
        """Перегружает строковое представление гориллы."""
        return f"{self.breed} по имени {self.name}, возраст: {self.age}"

    def make_sound(self) -> str:
        """Перегружает метод издания звука для горилл."""
        return "УУУУУУУУУУ!"

    def get_info(self) -> str:
        """Перегружает информацию о животном."""
        return f"Это горилла породы {self.breed}."
