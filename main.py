sideA  = int(input("Enter the first side: "))
sideB = int(input("Enter the second side: "))
sideC  = int(input("Enter the third side: "))

print("The triangle is", end=" ")
if sideA == sideB == sideC:
    print("equilateral")
else:
    print("not equilateral")