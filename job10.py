contenu=input("Saisissez le contenu : ")

f = open("output.txt" , "w")
f.write(contenu)
f.close()

f = open("output.txt", "r")
print(f.read())

f.close()