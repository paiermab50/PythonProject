def countvowels():
    y = ["a","e","i","o","u"]

    x=(input("Enter your string: ").lower())

    count = 0

    for i in x:
        if i in y:
            count+=1

    return f"The Count Is {count}"



