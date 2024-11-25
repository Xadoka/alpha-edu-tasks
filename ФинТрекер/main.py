from finance_tracker import FinanceTracker

def main():
    # Создаем объект системы финансового учета
    tracker = FinanceTracker()

    while True:
        print("\nЛичный Финансовый Трекер")
        print("1. Добавить Доход")
        print("2. Добавить Расход")
        print("3. Посмотреть Баланс")
        print("4. Посмотреть Транзакции")
        print("5. Генерация Отчета")
        print("6. Сохранить Данные")
        print("7. Загрузить Данные")
        print("8. Выход")

        choice = input("Введите ваш выбор: ")

        # Обработка выбора пользователя
        if choice == "1":
            amount = float(input("Введите сумму дохода: "))
            category = input("Введите категорию (например, Зарплата, Бизнес): ")
            tracker.add_income(amount, category)

        elif choice == "2":
            amount = float(input("Введите сумму расхода: "))
            category = input("Введите категорию (например, Еда, Транспорт): ")
            tracker.add_expense(amount, category)

        elif choice == "3":
            tracker.view_balance()

        elif choice == "4":
            tracker.view_transactions()

        elif choice == "5":
            tracker.generate_report()

        elif choice == "6":
            tracker.save_data()

        elif choice == "7":
            tracker.load_data()

        elif choice == "8":
            print("Выход из финансового трекера...")
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")

# Запуск основной программы
if __name__ == "__main__":
    main()