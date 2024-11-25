import json
from account_class import Account
from category_class import Category
from transaction_class import Transaction
import datetime

class FinanceTracker:
	def __init__(self):
		self.account = Account()

	def add_income(self, amount, category_name):
		category = Category(category_name)
		transaction = Transaction(amount,category)
		self.account.add_transaction(transaction)
		print(f"dfd ${amount} ff {category_name}.")