import random

passlen = int(input("Enter the password length: "))

s = "QWERTYUIOPLKJHGFDSAZXCVBNM0123456789qwertyuioplkjhgfdsazxcvbnm!@#$%^&*()"

p = "".join(random.sample(s, passlen))

print(p)