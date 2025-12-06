# src > main.py

class PageManager:
	def __init__(self):
		pass

class Node:
	def __init__(self):
		pass
	
class BPTree:
	def __init__(self):
		pass

	def insert(num):
		pass
		



def execute_query(query):
	message = ""
	if query.lower().startswith("show tables"):
		# Do something
		# 0. Need to create a table first.
            # 1. Figure out how a table is stored in a database file?
            # 2. Figure out how a row/tuple is stored of table stored in a database file?
            # 3. Figure out how to scan/read an entire table from the database file?
		pass
	else:
		message = "Incorrect query!"
	return message

def take_user_input(prompt):
	user_input = input(prompt)
	return user_input

def main():
	# Hello 
	query = take_user_input("Enter your query:\n")
	message = execute_query(query)
	print(message)

if __name__ == "__main__":
	main()
