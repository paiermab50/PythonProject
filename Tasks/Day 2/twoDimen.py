def two():
    x = int(input("Enter Your Number: "))
    list1 = []

    for i in range(1,x+1):
        list2= []
        for j in range(1,i+1):
            if i >= j:
                list2.append(i*j)
        list1.append(list2)        
        
    return list1
    del list2