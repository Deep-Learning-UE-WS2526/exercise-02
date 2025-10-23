while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    
    print("Enter operation (add/addition or multi/multiplication): ")
    operation = input().strip().lower()
    
    if operation in ["add", "addition"]:
        result = num1 + num2
        print("Sum: " + str(result))
    elif operation in ["multi", "multiplication"]:
        result = num1 * num2
        print("Product: " + str(result))
    else:
        print("Invalid operation!")
        continue
    
    print("Do you want to continue? (yes/y to continue, anything else to exit): ")
    continue_choice = input().strip().lower()
    
    if continue_choice not in ["yes", "y"]:
        print("Goodbye!")
        break