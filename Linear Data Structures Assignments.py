# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def getPairsCount(arr, n, sum):

	count = 0 # Initialize result

	# Consider all possible pairs
	# and check their sums
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
	getPairsCount(arr, n, sum))





# Q2. Write a program to reverse an array in place?

# Function to reverse A[] from start to end
def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)




# Q3. Write a program to check if two strings are a rotation of each other?

# Function checks if passed strings (str1 and str2)
# are rotations of each other
def areRotations(string1, string2):
	size1 = len(string1)
	size2 = len(string2)
	temp = ''

	# Check if sizes of two strings are same
	if size1 != size2:
		return 0

	# Create a temp string with value str1.str1
	temp = string1 + string1

	# Now check if str2 is a substring of temp
	# string.count returns the number of occurrences of
	# the second string in temp
	if (temp.count(string2)> 0):
		return 1
	else:
		return 0

# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
	print ("Strings are rotations of each other")
else:
	print ("Strings are not rotations of each other")




# Q4. Write a program to print the first non-repeated character from a string?

from collections import Counter

# Function which repeats
# first Nonrepeating character
def printNonrepeated(string):

	# Calculating frequencies
	# using Counter function
	freq = Counter(string)

	# Traverse the string
	for i in string:
		if(freq[i] == 1):
			print(i)
			break


# Driver code
string = "surajsrivastava"

# passing string to printNonrepeated function
printNonrepeated(string)




# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
		
# Driver code
n = 4
TowerOfHanoi(n, 'X', 'Y', 'Z')
# X, Y, Z are the name of rods




# Q6. Write a program to convert postfix to prefix expression.

# function to check if
# character is operator or not


def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False

# Convert postfix to Prefix expression


def postToPre(post_exp):

	s = []

	# length of expression
	length = len(post_exp)

	# reading from right to left
	for i in range(length):

		# check if symbol is operator
		if (isOperator(post_exp[i])):

			# pop two operands from stack
			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			# the operands and operator
			temp = post_exp[i] + op2 + op1

			# Push string temp back to stack
			s.append(temp)

		# if symbol is an operand
		else:

			# push the operand to the stack
			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans


# Driver Code
if __name__ == "__main__":

	post_exp = "XY*AB%"
	
	# Function call
	print("Prefix : ", postToPre(post_exp))






# Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
	stack = []
	
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
		
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
	str = "*-X/YZ-/XYZ"
	print(prefixToInfix(str))






# Q8. Write a program to check if all the brackets are closed in a given code snippet.

# closed brackets 

# function to check if
# brackets are closed


def areBracketsClosed(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsClosed(expr):
		print("Closed")
	else:
		print("Not Closed")





# Q9. Write a program to reverse a stack.

# stack using recursion

# Below is a recursive function
# that inserts an element
# at the bottom of a stack.
def insertAtBottom(stack, item):
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)

# Below is the function that
# reverses the given stack
# using insertAtBottom()
def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

# Below is a complete running
# program for testing above
# functions.

# Function to create a stack.
# It initializes size of stack
# as 0
def createStack():
	stack = []
	return stack

# Function to check if
# the stack is empty
def isEmpty( stack ):
	return len(stack) == 0

# Function to push an
# item to stack
def push( stack, item ):
	stack.append( item )

# Function to pop an
# item from stack
def pop( stack ):

	# If stack is empty
	# then error
	if(isEmpty( stack )):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack
def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end = ' ')
	print()

# Driver Code

stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)

reverse(stack)

print("Reversed Stack ")
prints(stack)






# Q10. Write a program to find the smallest number using a stack.

class Node:
	# Constructor which assign argument to node's value
	def __init__(self, value):
		self.value = value
		self.next = None

	# This method returns the string representation of the object.
	def __str__(self):
		return "Node({})".format(self.value)
	
	# __repr__ is same as __str__
	__repr__ = __str__


class Stack:
	# Stack Constructor initialise top of stack and counter.
	def __init__(self):
		self.top = None
		self.count = 0
		self.minimum = None
		
	# This method returns the string representation of the object (stack).
	def __str__(self):
		temp = self.top
		out = []
		while temp:
			out.append(str(temp.value))
			temp = temp.next
		out = '\n'.join(out)
		return ('Top {} \n\nStack :\n{}'.format(self.top,out))
		
	# __repr__ is same as __str__
	__repr__=__str__
	
	# This method is used to get minimum element of stack
	def getMin(self):
		if self.top is None:
			return "Stack is empty"
		else:
			print("Minimum Element in the stack is: {}" .format(self.minimum))



	# Method to check if Stack is Empty or not
	def isEmpty(self):
		# If top equals to None then stack is empty
		if self.top == None:
			return True
		else:
		# If top not equal to None then stack is empty
			return False

	# This method returns length of stack	
	def __len__(self):
		self.count = 0
		tempNode = self.top
		while tempNode:
			tempNode = tempNode.next
			self.count+=1
		return self.count

	# This method returns top of stack	
	def peek(self):
		if self.top is None:
			print ("Stack is empty")
		else:
			if self.top.value < self.minimum:
				print("Top Most Element is: {}" .format(self.minimum))
			else:
				print("Top Most Element is: {}" .format(self.top.value))

	# This method is used to add node to stack
	def push(self,value):
		if self.top is None:
			self.top = Node(value)
			self.minimum = value
		
		elif value < self.minimum:
			temp = (2 * value) - self.minimum
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.minimum = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}" .format(value))

	# This method is used to pop top of stack
	def pop(self):
		if self.top is None:
			print( "Stack is empty")
		else:
			removedNode = self.top.value
			self.top = self.top.next
			if removedNode < self.minimum:
				print ("Top Most Element Removed :{} " .format(self.minimum))
				self.minimum = ( ( 2 * self.minimum ) - removedNode )
			else:
				print ("Top Most Element Removed : {}" .format(removedNode))

				
			
	
# Driver program to test above class
stack = Stack()

stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()	
stack.pop()
stack.getMin()
stack.pop()
stack.peek()


