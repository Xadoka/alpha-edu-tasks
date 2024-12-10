import pandas as pd

# Загрузка данных из Excel
file_path = "Запрос на обслуживание.xlsx"  # Путь к вашему файлу
df = pd.read_excel(file_path)

print(df.head())  # Просмотр первых строк данных
