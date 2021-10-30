import string
import random

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+")

def generate_random_password():
	## define length of password
	length = 6

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))
 
## invoking the function
generate_random_password()