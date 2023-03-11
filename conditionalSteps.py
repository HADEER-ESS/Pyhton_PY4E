# conditional steps
x = int(input("Enter the X value... "))

if x < 10:
    print("X value is Smaller than 10")
    quit()
if 15 > x > 10:
    print("X value is Greater than 10 and smaller than 15")
    quit()

print("The Value Is Greater Than 15 UNEXPECTED :o")
