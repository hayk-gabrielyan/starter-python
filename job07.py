for i in range (0, 101):
    if i % 3 == 0 and i % 5 == 0:
        j = "FizzBuzz"
    elif i%3 == 0:
        j = "fizz"
    elif i%5 == 0:
        j = "buzz"
    else:
        j = i
    print(j)
    