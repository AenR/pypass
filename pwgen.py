import random

numbers = "0123456789"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

len = int(input("Please enter password length: "))

password = ''.join(random.choice(numbers + letters) for i in range(len))
print(password)