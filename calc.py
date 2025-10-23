def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter the operation (x, multi/multiplication for multiplication OR +, add/addition for addition): ")

    operation = str(input())
    if operation == "x" or operation == "multi" or operation == "multiplication":
        print("Product: " + str(num1*num2))
    if operation == "+" or operation == "add" or operation == "addition":
        print("Sum: " + str(num1+num2))
    abfrage()
    

def abfrage():
    print ("Exit? (Yes OR No): ")
    weiter = str(input())
    if weiter == "yes":
        calc()
    if weiter == "no":
        print ("Mach et jot!")

calc()
