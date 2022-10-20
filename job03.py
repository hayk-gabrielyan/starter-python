from itertools import zip_longest


age = input("Bonjour, quel âge as tu ?")
age=int(age)
if (age>=18):
    print("Tu es majeur")
else:
    print("Tu es mineur")