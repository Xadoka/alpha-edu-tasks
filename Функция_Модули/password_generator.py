import random
import datetime
import string

def get_password_length():
	while True:
		try:
			password_len = int(input("Введите длину пароля от 6 до 12: "))
		finally:
			except ValueError:
			print("Введите число")
		if(password_len >=6 and password_len<=12):
				return password_len
		else:
				print("Введите число от 6 до 12")

def include_special_characters():
	is_chat = input("Хотите спец символы(y/n): ")
	if is_chat.lower == 'y':
		return True
	else:
		return False
	
def generate_password(length, use_special_chars):
	list_of_all = [string.ascii_letters, string.digits]
	if (use_special_chars == True):
		list_of_all.append(string.punctuation)
	generated_password = " "
	for element in range(length):
		generated_password += random.choice(list_of_all)

def save_password(password):

def main:

if __name__ == "__main__":
    main()