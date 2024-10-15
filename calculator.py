def calculate(expression):
    try:
        result = eval(expression)  # функция eval вычисляет строку как математическое выражение
        return result
    except Exception as e:
        return f"Ошибка: {e}"

def main():
    print("Простой калькулятор")
    print("Введите 'y' для выхода")
    
    while True:
        expression = input("Введите выражение (пример: 128*2-112) : ")
        if expression.lower() == 'y':
            print("Выход из программы...")
            break
        
        result = calculate(expression)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
