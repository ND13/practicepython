import random, string

def generate_pw(length):
	password_chars = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(password_chars) for i in range(length))


pw_length = int(input("How long would you like your password: "))

print(generate_pw(pw_length))
