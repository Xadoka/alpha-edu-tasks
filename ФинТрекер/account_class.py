class Account:
	def __init__(self):
		self.balance = 0
		self.transactions = []

	def add_transaction(self,transaction):
		self.transactions.append(transaction)
		self.balance += transaction.amount

	def get_balance(self):
		return self.balance
	
	def get_transactions(self):
		return self.transactions
	
	def __str__(self):
		return str(self.balance)