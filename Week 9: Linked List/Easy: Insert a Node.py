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

# Function Arguments: head (refers to the head of the linked list
def insertSortedNode(head,value):
  temp= Node(value)
  if head== None:
    return temp
    
  if value< head.data:
    temp.next= head
    return temp

  curr= head
  while curr.next!= None and curr.next.data< value:
    curr= curr.next
    
  temp.next= curr.next
  curr.next= temp
  return head
	



def main():
	t = int(input())
	while (t != 0):
		singlyLinkedList = LinkedList()
		n = int(input())
		arr = list(map(int, input().split()))
		k = int(input())
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		singlyLinkedList.head=insertSortedNode(head,k)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
