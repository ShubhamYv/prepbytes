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

# First we will reverse the Linked List and then we will check whether the list is palindrome or not...
def reverseLinkedList(head):
  curr= head
  prev= None
  while curr!=None:
    next= curr.next
    curr.next= prev
    prev= curr
    curr= next
  return prev
  
# Function Arguments: head (refers to the head of the linked list)
def palindromeLlist(head):
  if head== None:
    return True
    
  slow, fast= head, head
  while(fast.next!=None and fast.next.next!=None):
    slow= slow.next
    fast= fast.next.next
    
  rev= reverseLinkedList(slow.next)
  curr=head
  while(rev!=None):
    if rev.data!= curr.data:
      return False
    rev= rev.next
    curr= curr.next
    
  return True
    

def main():
	t = int(input())
	while (t != 0):
		singlyLinkedList = LinkedList()
		n = int(input())
		arr = list(map(int, input().split()))
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		if(palindromeLlist(head)):
			print("true")
		else:
			print("false")
		t = t - 1


if __name__ == '__main__':
	main()
