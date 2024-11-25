import json
from account_class import Account
from category_class import Category
from transaction_class import Transaction
import datetime

class FinanceTracker:
	def __init__(self):
		self.account = Account()

	def add_income(self, amount, category_name):
		category = Category('eda')
		transac = Transaction(34,category)
		self.account.add_transaction(transac)
		print(f"Доход в размере ${amount} добавлен в категорию {category_name}.")
		
	def add_expense(self, amount, category_name):
		category = Category(category_name)
		transaction = Transaction(-amount,category)
		self.account.add_transaction(transaction)
		print(f"Расход в размере ${amount} добавлен в категорию {category_name}.")

	def view_balance(self):
		balance = self.account.get_balance()
		print(f"Ваш текущий баланс: ${balance}")

	def view_transactions(self):
		transactions = self.account.get_transactions()
		if not transactions:
			print("Транзакций не найдено.")
			return
		for transaction in transactions:
			print(transaction.display())  # Отображаем каждую транзакцию

	def generate_report(self):
		print("\nГенерация финансового отчета...")
		income = 0
		expenses = 0
		for transaction in self.account.get_transactions():
			if transaction.amount > 0:
				income += transaction.amount  # Суммируем доходы
			else:
				expenses += abs(transaction.amount)  # Суммируем расходы
		balance = self.account.get_balance()
		
		print(f"\nОбщий доход: ${income}")
		print(f"Общие расходы: ${expenses}")
		print(f"Баланс: ${balance}")

	def save_data(self, filename="finance_data.json"):
		data = {
    	"balance": self.account.get_balance(),
      "transactions": [{
      	"amount": t.amount,
        "category": t.category.name,
        "date": str(t.date)
      } for t in self.account.get_transactions()]
    }
        
		with open(filename, "w", encoding='utf-8') as file:
			json.dump(data, file, indent=4, ensure_ascii=False)
		print(f"Данные сохранены в {filename}.")

	def load_data(self, filename="finance_data.json"):
		try:
			with open(filename,"r",encoding="utf-8") as file:
				data = json.load(file)
				self.account.balance = data["balance"]
				for t_data in data["transaction"]:
					category = Category(t_data["category"])  
					date = datetime.datetime.strptime(t_data["date"], "%Y-%m-%d").date()  
					transaction = Transaction(t_data["amount"], category, date)  
					self.account.add_transaction(transaction) 
			print(f"Данные загружены из {filename}")
		except FileNotFoundError:
				print("Не удалось найти файл данных. Начинаем с пустого списка.")
		