class Stack:
	def __init__(self):
		self.items=[]
		# Initialise the stack's data attributes
		pass
	
	def push(self, item):
		self.items.insert(0,item)
		# Push an item to the stack 
		pass

	def peek(self):
		return self.items[0]
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		pass

	def pop(self):
		return self.items.pop(0)
		# Pop an item from the stack if non-empty 
		pass

	def is_empty(self):
		return self.items==[]
		# Return True if stack is empty, False otherwise
		pass 

	def __str__(self): 
		stack_string = ""
		for i in self.items:
			stack_string=stack_string+str(i)+" "
		stack_string = stack_string.rstrip()
		

		
		
			
		
		return stack_string    
 

		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		pass 

	def __len__(self):
		return len(self.items) 
		# Return current number of elements in the stack
		pass

