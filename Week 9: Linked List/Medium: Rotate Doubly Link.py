class Node:
	def __init__(self,data):
		self.data =data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtEnd(self,data):
		newNode = Node(data)
		if(self.head  is None):
			self.head=newNode
			self.tail=newNode
			return

		self.tail.next = newNode
		newNode.prev = self.tail
		self.tail= newNode

	def printDoublyLinkedList(self):
		temp=self.head
		while (temp is not None):
			print(temp.data, end=' ')
			temp = temp.next
		print()
    
# Function Arguments: head (refers to the head of the  doubly linked list) and k (denoting the number of positions to rotate)
def rotateDoublyList(head, k):
    if k == 0 :
        return head
    
    current = head

    count = 1
    while count < k and current != None :
        current = current.next
        count += 1
        
    if current == None :
        return head
      
    temp = current
    while current.next != None :
        current = current.next
        
    current.next = head
    head.prev = current
    head = temp.next
    head.prev = None
    temp.next = None
    return head
def main():
	t= int(input())
	while(t!=0):
		doublyLinkedList = DoublyLinkedList()
		n,k = map(int, input().split())
		arr = list(map(int, input().split()))
		for i in range(len(arr)):
			doublyLinkedList.insertAtEnd(arr[i])

		doublyLinkedList.head = rotateDoublyList(doublyLinkedList.head, k)
		doublyLinkedList.printDoublyLinkedList()
		t=t-1


if __name__ == '__main__':
	main()
