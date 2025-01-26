BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц

    def __str__(self):
        return f'Книга "{self.name}"'  # Возвращает строку с названием книги

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'  # Формат для создания объекта

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
