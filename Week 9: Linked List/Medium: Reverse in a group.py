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



# Function Arguments: head (refers to the head of the linked list) and k (denoting the group size)
def reverseKnodes(head,k):
    curr= head
    next= None
    prev= None
    count=0
    while(curr!=None and count<k):
        next= curr.next
        curr.next= prev
        prev= curr
        curr= next
        count+=1
    if(next!= None):
        rest_head= reverseKnodes(next, k)
        head.next= rest_head
        
    return prev
    
      

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
		singlyLinkedList.head=reverseKnodes(head,k)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
