from abc import ABC, abstractmethod
from typing import Any, List

class Table(ABC):
    """
    Абстрактный класс, описывающий стол.
    """

    def __init__(self, material: str, height: float):
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        self.material = material
        self.height = height

    @abstractmethod
    def fold(self) -> None:
        """
        Сложить стол.
        """
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Переместить стол в новое место.

        Args:
            new_location (str): Новое местоположение.
        """
        ...

class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.species = species
        self.age = age

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Выполнить процесс фотосинтеза.
        """
        ...

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева на заданное количество лет.

        Args:
            years (int): Количество лет для роста. Должно быть положительным числом.

        Raises:
            ValueError: Если передано отрицательное число.

        Example:
            >>> tree.grow(5)
        """
        ...

class SocialMediaPlatform(ABC):
    """
    Абстрактный класс, описывающий социальную платформу.
    """

    def __init__(self, name: str, active_users: int):
        if active_users < 0:
            raise ValueError("Number of active users cannot be negative.")
        self.name = name
        self.active_users = active_users

    @abstractmethod
    def post_content(self, content: str) -> None:
        """
        Разместить контент на платформе.

        Args:
            content (str): Текст контента для публикации.

        Example:
            >>> platform.post_content("Hello, world!")
        """
        ...

    @abstractmethod
    def ban_user(self, user_id: int) -> None:
        """
        Заблокировать пользователя на платформе.

        Args:
            user_id (int): Идентификатор пользователя.

        Example:
            >>> platform.ban_user(12345)
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
