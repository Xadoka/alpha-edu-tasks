import random
import string

def generate_password(length=12, use_symbols=True):
    """Генератор пароля заданной длины с возможностью выбора символов."""
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")

    # Наборы символов для пароля
    letters = string.ascii_letters  # Буквы (строчные и заглавные)
    digits = string.digits          # Цифры
    symbols = "!@#$%^&*()-_+="      # Специальные символы

    # Формируем допустимый набор символов
    all_characters = letters + digits
    if use_symbols:
        all_characters += symbols

    # Гарантируем наличие хотя бы одного символа каждого типа
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(letters.upper()),  # Заглавная буква
    ]
    if use_symbols:
        password.append(random.choice(symbols))

    # Добавляем оставшиеся символы случайным образом
    password += random.choices(all_characters, k=length - len(password))

    # Перемешиваем символы для большей случайности
    random.shuffle(password)

    # Возвращаем пароль как строку
    return ''.join(password)

def main():
    print("Добро пожаловать в генератор паролей!")
    while True:
        try:
            # Запрашиваем длину пароля
            length = int(input("Введите длину пароля (не менее 4 символов): "))
            if length < 4:
                raise ValueError("Длина пароля должна быть не менее 4 символов.")

            # Запрашиваем, нужны ли специальные символы
            use_symbols_input = input("Нужны ли специальные символы? (да/нет): ").strip().lower()
            use_symbols = use_symbols_input in ('да', 'yes', 'y')

            # Генерируем и выводим пароль
            password = generate_password(length, use_symbols)
            print("Сгенерированный пароль:", password)
            
            # Спрашиваем, хочет ли пользователь сгенерировать ещё пароль
            another = input("Хотите сгенерировать ещё один пароль? (да/нет): ").strip().lower()
            if another not in ('да', 'yes', 'y'):
                print("Спасибо за использование генератора паролей!")
                break
        except ValueError as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    main()
