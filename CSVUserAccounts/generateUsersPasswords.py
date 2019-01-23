# Alexy DA CRUZ 2019 - CSV Accounts
import csv
from random import *
import string

chemin = "comptes.csv"
new_chemin = "new_comptes.csv"

users = []

# List that contains the header
def HeaderList():
	return ["NAME", "FIRST NAME", "CLASS", "LOGIN", "PASSWORD"]

# Generate a password of 6 chars
def GeneratePassword():
	password = []
	for i in range(6):
		id = randrange(1,27)
		password.append(string.ascii_letters[id])
	return ''.join(password)

# Generate a username with the 5 first chars of the name concatened with the first letter of the firstname
def GenerateUsername(name, firstname):
	name = name.replace(' ', '')
	username_list = []
	
	for i in range(5):
		username_list.append(name[i])
	username_list.append(firstname[0])
	return ''.join(username_list)

def Accounts():
	return []

def Save(accounts):
	with open(new_chemin, 'w', newline='') as csvfile:
		c = csv.writer(csvfile, delimiter=';')
		c.writerow(HeaderList())
		for data in accounts:
			c.writerow(data)
	csvfile.close()

# Main function
def Main():
	with open(chemin, 'r') as csvfile: 
		next(csvfile)
		ac = csv.reader(csvfile, delimiter=';')
		users = []
		for row in ac:
			user = [row[0], row[1], row[2], GenerateUsername(str(row[0]), str(row[1])), GeneratePassword()]
			users.append(user)
		Save(users)

# Call the main function at launch
if __name__ =='__main__':
	Main()
