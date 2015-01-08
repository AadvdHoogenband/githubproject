def calculator():
	
	x = int(raw_input("First number: "))
	y = int(raw_input("Second number: "))

	if operation == "Multiply" :
		print "The answer is ",
		print x * y
   
	elif operation == "Add" :
		print "The answer is ",
		print x + y
	
	elif operation == "Divide" :
		print "The answer is ",
		print x / y
		
def calc():
	
	global operation
	operation = raw_input("Do you want to Multiply, Divide or Add: ")
	if operation == "Multiply" :
		calculator()
	elif operation == "Divide" : 
		calculator()
	elif operation == "Add" :
		calculator()
	else:
		print "That's not a correct calculation, Try again"
		calc()

answer = 1 

	
calc()


