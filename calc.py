def exercise():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    
    # 1
    operation = input("Addition or multiplication? ")
    
    # 2
    if operation == "add" or operation == "addition":
        print("Sum: " + str(num1+num2))
    elif operation == "multi" or operation == "multiplication":
        print("Product: " + str(num1*num2))
    else:
        print("Invalid operation.")
    
def main():
    # 3
    while True:
        exercise()
        continuation = input("Do you wish to continue? (y/n) ")
        if continuation != "y":
            break
            
if __name__ == "__main__":
    main()
