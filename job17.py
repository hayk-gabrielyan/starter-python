def myFonction(*params):
    myList = []

    for param in params:
        if isinstance(param, (int)):
            myList.append(param)
            
        else:
            print("Attention un des paramètres n'est pas numérique")
    
    for element in myList:
        if element % 2 == 0:
            print(element)
    
myFonction(3,6,9,12,15,18,22)