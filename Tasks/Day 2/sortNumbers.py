def sort():
    list = []
    for i in range(5):
        num = input(f"Enter Number {i+1}: ")
        if num.isdigit():
            list.append(num)
        else:
            print("Enter a valid number.")
            return sort()
    print(sorted(list))
    print(sorted(list, reverse=True))
    
#---------------------------------------------------
# Without for loop

# num = input("Enter 5 Numbers seperated by , :")
# x = num.split(",")
# print(sorted(x))
# print(sorted(x, reverse=True))