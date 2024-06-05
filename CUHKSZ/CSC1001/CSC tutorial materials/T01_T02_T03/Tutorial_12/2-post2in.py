# Python3 program to find infix for 
# a given postfix. 
def isOperand(x):
	return ((x >= 'a' and x <= 'z') or
			(x >= 'A' and x <= 'Z')) 

# Get Infix for a given postfix 
# expression 
def getInfix(exp) :

	s = [] 

	for i in exp:	 
		
		# Push operands 
		if (isOperand(i)) :		 
			s.insert(0, i) 
			
		# We assume that input is a 
		# valid postfix and expect 
		# an operator. 
		else:
		
			op1 = s[0] 
			s.pop(0) 
			op2 = s[0] 
			s.pop(0) 
			s.insert(0, "(" + op2 + i +
							op1 + ")") 
			
	# There must be a single element in 
	# stack now which is the required 
	# infix. 
	return s[0]

# Driver Code 
if __name__ == '__main__': 

	exp = "ABC-D*+"
	print(getInfix(exp.strip()))
	exp = "XYZ+AB-*-"
	print(getInfix(exp.strip()))
	exp = "AB+CD-/E+"
	print(getInfix(exp.strip()))
	exp = "AB+C-DE*+"
	print(getInfix(exp.strip()))
# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
