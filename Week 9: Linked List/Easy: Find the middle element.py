class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtEnd(self, data):
		newNode = Node(data)
		if (self.head is None):
			self.head = newNode
			self.tail = newNode
			return self.head

		else:
			self.tail.next = newNode
			self.tail = newNode
			return self.head

	def printSinglyLinkedList(self):
		temp = self.head
		while (temp is not None):
			print(temp.data, end=' ')
			temp = temp.next
		print()

# Function Arguments: head (refers to the head of the linked list)
def printMidElement(head):
	if head== None:
	  return
	slow= head
	fast= head
	while(fast!= None and fast.next!=None):
	  slow= slow.next
	  fast= fast.next.next
	print(slow.data)

  
def main():
	t = int(input())
	while (t != 0):
		singlyLinkedList = LinkedList()
		n = int(input())
		arr = list(map(int, input().split()))
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		printMidElement(head)
		t = t - 1


if __name__ == '__main__':
	main()
