largest = None
smallest = None

while True:
    inputNum = input("Enter a number:")
    try:
        num = int(inputNum)
        if largest is None:
            largest = num
            # print("The largest num ", largest)
        if smallest is None:
            smallest = num
            # print("The smallest num ", smallest)
        elif largest < num:
            largest = num
            # print("The largest num becomessssss", largest)
        elif smallest > num:
            smallest = num
            # print("The smallest num becomessssss", smallest)
    except:
        if inputNum == "done":
            print("Maximum is", largest)
            print("Minimum is", smallest)
            break
        else:
            print("invalid input")
            continue
