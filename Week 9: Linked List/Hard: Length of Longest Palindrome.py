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


    
    
def countCommon(a, b) :
    count = 0
    while ( a != None and b != None ) :
        if (a.data == b.data) :
            count = count + 1
        else:
            break
        a = a.next
        b = b.next
    return count 

def longestPalindrome(head):
    result = 0
    prev = None
    curr = head 
    while (curr != None) : 
        next = curr.next
        curr.next = prev
        result = max(result, 2 * countCommon(prev, next) + 1)
        result = max(result, 2 * countCommon(curr, next))
        prev = curr 
        curr = next
    return result



def main():
	t = 1
	while (t != 0):
		singlyLinkedList = LinkedList()
		n= int(input())
		arr = list(map(int, input().split()))
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		print(longestPalindrome(head))
		t = t - 1


if __name__ == '__main__':
	main()
