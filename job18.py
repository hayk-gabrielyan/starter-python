def myFonction(*params):
    myList = []

    for i in params:
        myList.append(i)
        myList.sort()
    print(myList)

myFonction(15,3,22,6,1,12,35,18,21)
