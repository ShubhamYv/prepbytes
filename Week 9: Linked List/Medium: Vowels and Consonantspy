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
    

def arrangeVowCon(head):
    vowel = None
    consonant = None
    start = None
    end = None
    while (head != None):
        x = head.data
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            if (vowel == None):
                vowel =  Node(x);
                start = vowel;
            else:
                vowel.next =  Node(x)
                vowel = vowel.next
        else:
            if (consonant == None):
                consonant =  Node(x)
                end = consonant
            else:
                consonant.next =  Node(x)
                consonant = consonant.next
        head = head.next
    if (start == None):
        return end
    vowel.next = end
    return start
def main():
	t = int(input())
	while (t!= 0):
		singlyLinkedList = LinkedList()
		n = int(input())
		arr = list(input().split())
		head = None
		for i in range(n):
			head = singlyLinkedList.insertAtEnd(arr[i])
		singlyLinkedList.head=arrangeVowCon(head)
		singlyLinkedList.printSinglyLinkedList()
		t = t - 1


if __name__ == '__main__':
	main()
