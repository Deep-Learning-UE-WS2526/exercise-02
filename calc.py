


while True:
    print("Enter number 1: ")
    num1 = int(input())

    print("Enter number 2: ")
    num2 = int(input())

    op = input("Operation (add/addition or multi/multiplication): ").strip().lower()

    if op == "add" or op == "addition":
        print("Sum: " + str(num1 + num2))
    elif op == "multi" or op == "multiplication":
        print("Product: " + str(num1 * num2))
    else:
        print("Unknown operation. Use add/addition or multi/multiplication.")
        continue

    cont = input("Continue? (type yes to continue): ").strip().lower()
    if cont != "yes":
        break
