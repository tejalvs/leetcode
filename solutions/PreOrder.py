class newNode:  
  
   
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None

'''def inOrder(root):

	current=root
	stack=[]
	while(True):
		if current is not None:
			stack.append(current)
			current=current.left

		elif(len(stack)!=0):
			current=stack.pop()
			print(current.data)
			current=current.right

		else:
			break'''


def preOrder(root):

	current=root
	stack=[]
	while(True):
		stack.append(current)
		if current is not None:
			current=current.left

		elif(len(stack)!=0):
			print(current.data)
			current=stack.pop()
			current=current.right

		else:
			break




if __name__ == '__main__': 
      
	root = newNode(1) 
	root.left = newNode(2) 
	root.right = newNode(3) 
	root.left.left = newNode(4) 
	root.left.right = newNode(5) 
  
#inOrder(root) 
preOrder(root)