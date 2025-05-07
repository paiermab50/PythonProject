def countI():
    
    x = input("Enter your string: ").lower()
    counter = 0
    for i in x:
        if i == "i":
            counter+=1
            x=list(x)
            x[x.index(i)] = "t"
        if counter == 0:
            return "You have not eneterd any Is"
    return f"{counter} Is the numbers of i"