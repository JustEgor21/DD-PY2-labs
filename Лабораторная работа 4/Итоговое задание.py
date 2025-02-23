from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._health_status = "Healthy"  # Закрытый атрибут, так как он не должен изменяться извне

    def __str__(self) -> str:
        return f"{self.name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    @abstractmethod
    def make_sound(self) -> None:
        """
        Абстрактный метод, который должны реализовать дочерние классы.
        """
        pass

    def get_health_status(self) -> str:
        """
        Получение состояния здоровья животного.
        """
        return self._health_status


class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        return f"Собака {self.name}, порода {self.breed}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> None:
        print("Гав-гав!")


# Вторая сущность: Музыкальные инструменты
class MusicalInstrument(ABC):
    """
    Базовый класс для музыкальных инструментов.
    """

    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material

    def __str__(self) -> str:
        return f"{self.name} из материала {self.material}"

    def __repr__(self) -> str:
        return f"MusicalInstrument(name={self.name}, material={self.material})"

    @abstractmethod
    def play_sound(self) -> None:
        pass


class Guitar(MusicalInstrument):
    """
    Дочерний класс для гитары.
    """

    def __init__(self, name: str, material: str, string_count: int):
        super().__init__(name, material)
        self.string_count = string_count

    def __str__(self) -> str:
        return f"Гитара {self.name}, {self.string_count} струн, материал {self.material}"

    def play_sound(self) -> None:
        print("Бринь-бринь")


# Третья сущность: Компьютерные устройства
class ComputerDevice(ABC):
    """
    Базовый класс для компьютерных устройств.
    """

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"ComputerDevice(brand={self.brand}, model={self.model})"

    @abstractmethod
    def connect(self) -> None:
        pass


class Laptop(ComputerDevice):
    """
    Дочерний класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, battery_life: int):
        super().__init__(brand, model)
        self.battery_life = battery_life

    def __str__(self) -> str:
        return f"Ноутбук {self.brand} {self.model}, батарея {self.battery_life} часов"

    def connect(self) -> None:
        print("Подключение к сети Wi-Fi...")


if __name__ == "__main__":
    dog = Dog("Шарик", 3, "Лабрадор")
    print(dog)
    dog.make_sound()

    guitar = Guitar("Yamaha", "дерево", 6)
    print(guitar)
    guitar.play_sound()

    laptop = Laptop("Apple", "MacBook Pro", 10)
    print(laptop)
    laptop.connect()

