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


    
    
    
    
    
    
def reverse(head):
    prev = None   
    curr = head
    while (curr):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def reverseInRange(head, m, n):
    if (m == n):
        return head
    revs = None
    revs_prev = None
    revend = None
    revend_next = None
    i = 1
    curr = head
    while (curr and i <= n):
        if (i < m):
            revs_prev = curr
   
        if (i == m):
            revs = curr
   
        if (i == n):
            revend = curr
            revend_next = curr.next
   
        curr = curr.next
        i += 1
  
    revend.next = None
    revend = reverse(revs)
    if (revs_prev):
        revs_prev.next = revend
    else:
        head = revend
    revs.next = revend_next
    return head



def main():
	t = 1
	while (t != 0):
		singlyLinkedList = LinkedList()
		n,l,r = map(int, input().split())
		arr = list(map(int, input().split()))
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		singlyLinkedList.head=reverseInRange(head,l,r)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
