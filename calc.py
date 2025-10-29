def myFunction(): 
	print("Enter number 1: ")
	num1 = int(input())
	print("Enter number 2: ")
	num2 = int(input())
	#print("Choose operation (add|multiply): ")

	#trying out switch statements. .lower() turns user input into lowercase letters. 
	#input is a "built-in" function that basically works like scanners in Java
	#the input is stored in the variable choice which is then used in the following switch statement
	choice = input("Choose operation (add|multiply)").lower()
	#match seems to be the Python equivalent of the switch Keyword 
	match choice:
		case "add":
			result = num1 + num2
			#Typecasting int result to String otherwise the program breaks
			print("Sum: " + str(result))
		case "multiply":
			result = num1 * num2
			print("Product: " + str(result))
		#default cases use the _ 
		case _:
			print("Something went wrong. Maybe a Spelling error?")
	
	print("Press 'X' to repeat|Press Enter to exit.")	
	#here the input() Method (The Scanner) pauses again until the user types sth. The Input is changed to lowercase
	userInput = input().lower()
	if userInput == "x":
		myFunction()
	#If the Input is an empty String, the program exits
	elif userInput() == "":
		print("Exiting...")
		#return seems to work aswell, return exits the current function. exit() terminates the whole program
		#exit()
		return
myFunction()