print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
#print("Choose operation (add|multiply): ")

#trying switch statements. .lower() turns user input into lowercase letters
choice = input("Choose operation (add|multiply)").lower()
match choice:
	case "add":
		result = num1+num2
		print("Sum: " + str(result))
	case "multiply":
		result = num1*num2
		print("Product: " + str(result))
	case _:
		print("Something went wrong. Maybe a Spelling error?")
		
input("Press Enter to exit")
#print("Sum: " + str(num1+num2))
#print("Product: " + str(num1*num2))