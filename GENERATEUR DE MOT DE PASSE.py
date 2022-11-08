import random
import string



## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%&*()_={}&<>?/|")
characters = list(string.ascii_letters + string.digits + "!@#$%&*()_={}&<>?/|")


def generate_random_password():
	## length of password from the user
	length = int(input("Entrer la longueur du mot de passe souhaiter : "))

	## number of character types
	alphabets_count = 1
	digits_count = 1
	special_characters_count = 1

	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("Le nombre total de caractères est supérieur à la longueur du mot de passe")
		return

	## initializing the password
	password = []

	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))

	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))

	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))


## invoking the function
generate_random_password()
input("Press enter to exit ;)")
