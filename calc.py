import sys

while True:
    op = input("Operation (add/addition or multi/multiplication): ").strip()
    if op not in ("add", "addition", "multi", "multiplication"):
        continue  

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if op in ("add", "addition"):
        print("Sum: " + str(num1 + num2))
    else:
        print("Product: " + str(num1 * num2))

    while True:
        c = input("Do you want to continue? (yes/Yes or no/No): ").strip()
        if c in ("yes", "Yes"):
            break  #bei nächste Runde weitermachen
        if c in ("no", "No"):
            print("Program exited.") # Programm wird beendet
            sys.exit(0)