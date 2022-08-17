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
def removeDuplicates(head):
  curr= head
  while(curr!= None and curr.next != None):
    if(curr.data == curr.next.data):
      curr.next= curr.next.next
    else:
      curr= curr.next
  return head


def main():
	t = int(input())
	while (t != 0):
		singlyLinkedList = LinkedList()
		n = int(input())
		arr = list(map(int, input().split()))
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		singlyLinkedList.head=removeDuplicates(head)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
