import sqlite3
from datetime import datetime

# Класс для управления библиотекой
class Bookstore:
    def __init__(self, db_name="bookstore.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author VARCHAR(255) NOT NULL,
            year DATE NOT NULL,
            genre TEXT NOT NULL,
            price REAL NOT NULL,
            amount INTEGER NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_book(self, title, author, year, genre, price, amount):
        query = "INSERT INTO books (title, author, year, genre, price, amount) VALUES (?, ?, ?, ?, ?, ?)"
        self.connection.execute(query, (title, author, year, genre, price, amount))
        self.connection.commit()
        print("Книга добавлена!")

    def remove_book(self, book_id):
        query = "DELETE FROM books WHERE id = ?"
        self.connection.execute(query, (book_id,))
        self.connection.commit()
        print("Книга удалена!")

    def update_book(self, book_id, field, new_value):
        query = f"UPDATE books SET {field} = ? WHERE id = ?"
        self.connection.execute(query, (new_value, book_id))
        self.connection.commit()
        print("Информация о книге обновлена!")

    def search_books(self, **criteria):
        query = "SELECT * FROM books WHERE " + " AND ".join(f"{key} LIKE ?" for key in criteria)
        values = [f"%{value}%" for value in criteria.values()]
        cursor = self.connection.execute(query, values)
        results = cursor.fetchall()
        return results

    def get_all_books(self):
        query = "SELECT * FROM books"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

# Класс покупателя
class Person:
    def __init__(self, bookstore):
        self.bookstore = bookstore

    def search_books(self, **criteria):
        books = self.bookstore.search_books(**criteria)
        if books:
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Жанр: {book[4]}, Цена: {book[5]}, Количество: {book[6]}")
        else:
            print("Книги не найдены.")

    def buy_book(self, book_id):
        query = "SELECT amount FROM books WHERE id = ?"
        cursor = self.bookstore.connection.execute(query, (book_id,))
        book = cursor.fetchone()
        if book and book[0] > 0:
            self.bookstore.update_book(book_id, "amount", book[0] - 1)
            print("Книга успешно куплена!")
        else:
            print("Книга закончилась.")

# Текстовое меню
def menu():
    bookstore = Bookstore()
    user = Person(bookstore)

    while True:
        print("\nМеню:")
        print("1. Добавить книгу (администратор)")
        print("2. Удалить книгу (администратор)")
        print("3. Обновить данные книги (администратор)")
        print("4. Поиск книги")
        print("5. Купить книгу")
        print("6. Показать все книги")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год выпуска (YYYY-MM-DD): ")
            genre = input("Введите жанр книги: ")
            price = float(input("Введите цену книги: "))
            amount = int(input("Введите количество экземпляров: "))
            bookstore.add_book(title, author, year, genre, price, amount)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            bookstore.remove_book(book_id)

        elif choice == "3":
            book_id = int(input("Введите ID книги для обновления: "))
            field = input("Введите поле для обновления (title, author, year, genre, price, amount): ")
            new_value = input("Введите новое значение: ")
            if field in ["price", "amount"]:
                new_value = float(new_value) if field == "price" else int(new_value)
            bookstore.update_book(book_id, field, new_value)

        elif choice == "4":
            criteria = {}
            title = input("Введите название книги (оставьте пустым для пропуска): ")
            author = input("Введите автора книги (оставьте пустым для пропуска): ")
            year = input("Введите год выпуска (оставьте пустым для пропуска): ")
            genre = input("Введите жанр книги (оставьте пустым для пропуска): ")
            if title: criteria["title"] = title
            if author: criteria["author"] = author
            if year: criteria["year"] = year
            if genre: criteria["genre"] = genre
            user.search_books(**criteria)

        elif choice == "5":
            book_id = int(input("Введите ID книги для покупки: "))
            user.buy_book(book_id)

        elif choice == "6":
            books = bookstore.get_all_books()
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Жанр: {book[4]}, Цена: {book[5]}, Количество: {book[6]}")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    menu()
