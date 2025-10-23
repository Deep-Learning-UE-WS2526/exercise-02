def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operation (+/a/add/addition or */x/m/mult/multiplication) ")
    operation = input()

    if operation in ["+", "a", "add", "addition"]:
        print("Sum: " + str(num1+num2))
    elif operation in ["*", "x", "m", "mult", "multiplication"]:
        print("Product: " + str(num1*num2))
    else:
        print("Invalid operation")

    print("Calculation complete.")
    print("Do you want to perform another calculation? (y/n)")
    choice = input()
    if choice.lower() == "y":
        calc()
    else:
        print("Exiting calculator.")


calc()
