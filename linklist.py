class Node:
	"Node Class:Create Nodes"
	def __init__(self,value):
		self.value = value 
		self.next = None


class linklist:
	"Link List Class:Linklist Operation"
	def __init__(self):
		self.head = None

	def insert(self,value):
		newNode = Node(value)

		if self.head is None:
			self.head = newNode
		else:
			tempNode = self.head
			while tempNode.next is not None:
				tempNode = tempNode.next
			tempNode.next = newNode
	
	def search(self,value):
		tempNode = self.head
		prevTempNode = None 
		while  tempNode is not None and tempNode.value is not value:
			prevTempNode = tempNode
			tempNode = tempNode.next
		if tempNode is None:
			return "Node not Present"
		else:
			return "Node is Present",prevTempNode

	def delete(self,value):
		status,prevNode = self.search(value)
		if status == "Node is Present":
			if prevNode == None:
				self.head = self.head.next
			else:
				prevNode.next = prevNode.next.next
		else:
			print("value %s is Not Present",value)
	
	def printlist(self):
		tempNode = self.head
		while tempNode is not None:
			print(tempNode.value)
			tempNode = tempNode.next


l = linklist()
l.insert(10)
l.insert(20)
l.insert(30)
status,_ = l.search(20)
print(status)

l.delete(10)
l.printlist()
