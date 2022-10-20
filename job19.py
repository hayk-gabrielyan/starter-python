def myFonction(*params):
    myList = []

    for i in params:
        if isinstance(i, (int)):
            myList.append(i)
            myList.sort()
        else:
            print("Attention un des paramètres n'est pas numérique")
        
    print(myList)

myFonction(15,3,22,6,1,12,35,18,21)
