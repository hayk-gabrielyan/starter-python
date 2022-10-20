a = input('valeur-1 : ')
a=int(a)
b = input('valeur-2 : ')
b=int(b)

if (a<b):
    for i in range (a+1, b, 1):
        print(i)

else:
    for i in range (a-1, b, -1):
        print(i)

if (a==b): 
    print('valeurs égales')

