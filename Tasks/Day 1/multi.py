def multiplier():
    x = int(input("Enter Your Number: "))

    for i in range(1,x+1):
        for j in range(1,i+1):
            if i >= j:
                print(f" {i}*{j} = {i*j}")