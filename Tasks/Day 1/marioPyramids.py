def mario():
    x = int(input("Enter your pyramid's layer: "))

    for i in range(1,x+1):
        print((" "*(x-i))+("*"*i))
    
