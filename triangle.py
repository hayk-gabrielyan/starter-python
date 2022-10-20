left = "/"
right= "\\"
base= "_"

hauteur = int(input("Saisissez la hauteur : "))

for i in range(hauteur):
    print((hauteur -i) * " " + left + ((i * 2) * " ") + right)
    if i == hauteur -1:
        print(left + base * (hauteur *2) + right)

