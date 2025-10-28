import operator
ops = {
    "+": operator.add,
    "add": operator.add,
    "addition": operator.add,
    "*": operator.mul,
    "multi": operator.mul,
    "multiplication": operator.mul
}
def start():
    print("Enter number 1: ")
    num1 = int(input())

    print("Enter number 2: ")
    num2 = int(input())

    print("Enter operator: ")
    opInput = str(input())

    op = ops.get(opInput)
    print("Solution: "+ str(op(num1, num2)))

    print("Do you want to continue (y/n)?")
    confirm = input()
    if confirm == "y":
        print("Starting over..")
        start()
    elif confirm == "n":
        print("exiting..")
        SystemExit

start()