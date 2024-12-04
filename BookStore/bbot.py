from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import sqlite3
from datetime import datetime

# Класс управления библиотекой
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

    def remove_book(self, book_id):
        query = "DELETE FROM books WHERE id = ?"
        self.connection.execute(query, (book_id,))
        self.connection.commit()

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

    def buy_book(self, book_id):
        query = "SELECT amount FROM books WHERE id = ?"
        cursor = self.connection.execute(query, (book_id,))
        book = cursor.fetchone()
        if book and book[0] > 0:
            self.update_book(book_id, "amount", book[0] - 1)
            return True
        return False

    def update_book(self, book_id, field, new_value):
        query = f"UPDATE books SET {field} = ? WHERE id = ?"
        self.connection.execute(query, (new_value, book_id))
        self.connection.commit()

# Создаем экземпляр библиотеки
bookstore = Bookstore()

# Команды Telegram-бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для управления библиотекой.\n"
        "Доступные команды:\n"
        "/add — Добавить книгу\n"
        "/list — Показать все книги\n"
        "/search — Поиск книги\n"
        "/buy — Купить книгу"
    )

async def add_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = " ".join(context.args)
        title, author, year, genre, price, amount = data.split(",")
        bookstore.add_book(title.strip(), author.strip(), year.strip(), genre.strip(), float(price), int(amount))
        await update.message.reply_text("Книга успешно добавлена!")
    except Exception as e:
        await update.message.reply_text(f"Ошибка при добавлении книги: {e}\nФормат: /add Название, Автор, Год (YYYY-MM-DD), Жанр, Цена, Количество")

async def list_books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    books = bookstore.get_all_books()
    if books:
        message = "\n".join(
            f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Жанр: {book[4]}, Цена: {book[5]}, Количество: {book[6]}"
            for book in books
        )
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Книг пока нет в библиотеке.")

async def search_books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    criteria = {}
    try:
        data = " ".join(context.args)
        params = data.split(",")
        for param in params:
            key, value = param.split("=")
            criteria[key.strip()] = value.strip()
        books = bookstore.search_books(**criteria)
        if books:
            message = "\n".join(
                f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Жанр: {book[4]}, Цена: {book[5]}, Количество: {book[6]}"
                for book in books
            )
            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Книги по заданным критериям не найдены.")
    except Exception as e:
        await update.message.reply_text(f"Ошибка при поиске книг: {e}\nФормат: /search ключ=значение, ключ=значение")

async def buy_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        book_id = int(context.args[0])
        if bookstore.buy_book(book_id):
            await update.message.reply_text("Книга успешно куплена!")
        else:
            await update.message.reply_text("Книга закончилась или не найдена.")
    except Exception as e:
        await update.message.reply_text(f"Ошибка при покупке книги: {e}\nФормат: /buy ID_книги")

# Создание и запуск бота
def main():
    application = ApplicationBuilder().token("ВАШ_ТОКЕН_БОТА").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_book))
    application.add_handler(CommandHandler("list", list_books))
    application.add_handler(CommandHandler("search", search_books))
    application.add_handler(CommandHandler("buy", buy_book))

    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
