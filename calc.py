on = True
while on:  
    on = False
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operation (mulitiplication/ mutli/ * or addition/ add/ +): ")
    op = input()
    if op == "multiplication" or op == "multi" or op == "*":
        print("Product: " + str(num1*num2))
    if op == "addition" or op == "add" or op == "+":
        print("Sum: " + str(num1+num2))
    print("To continue, enter y.")
    on = input() == "y"

    