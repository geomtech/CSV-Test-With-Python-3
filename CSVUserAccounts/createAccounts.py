# Alexy DA CRUZ 2019 - CSV Accounts
import csv

# Variables
chemin = "comptes.csv"

# List that contains users lists
def Accounts():
	return [		
		["DA CRUZ", "Alexy", "SIO1", "", ""],
		["DEZANDRE", "William", "SIO1", "",""],
		["SAISON", "Axel", "SIO1", "",""],
		["LAFON", "Vincent", "SIO1", "",""]
		]

# List that contains the header
def HeaderList():
	return ["NAME", "FIRST NAME", "CLASS", "LOGIN", "PASSWORD"]

# Main function
def Main():
	print("createAccounts.py")
	with open(chemin, 'w', newline='') as csvfile:
		c = csv.writer(csvfile, delimiter=';')
		c.writerow(HeaderList())
		for data in Accounts():
			c.writerow(data)
	csvfile.close()

# Call the main function at launch
if __name__ =='__main__':
	Main()