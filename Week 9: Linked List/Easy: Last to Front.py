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
def lastElementFirst(head):
    if head.next== None:
        return head
    temp = head
    sec_last = None
    # if not temp or not temp.next: 
    #     return
    while temp and temp.next :
        sec_last = temp
        temp = temp.next
    sec_last.next = None
    temp.next = head
    head = temp
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
		singlyLinkedList.head=lastElementFirst(head)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
