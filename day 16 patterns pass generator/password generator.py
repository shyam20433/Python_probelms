import random,string

letters=string.ascii_letters
numbers=string.digits
digits=string.digits
print(''.join(random.choices((letters+digits+numbers),k=10)))