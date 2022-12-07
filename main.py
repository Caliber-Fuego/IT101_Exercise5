firstNum  = int(input("Enter the first side: "))
secondNum = int(input("Enter the second side: "))
thirdNum  = int(input("Enter the third side: "))

print("The triangle is", end=" ")
if firstNum == secondNum == thirdNum:
    print("equilateral")
else:
    print("not equilateral")