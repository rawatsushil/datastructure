class LinkedList():	
	def __init__(self, val):
		self.val = val
		self.next = None

def display(head):
	while(head):
		print (head.val)
		head = head.next

def mergeSortLinkedList(A):
	if A is None or A.next is None:
		return A
	leftHalf, rightHalf = splitList(A)
	left = mergeSortLinkedList(leftHalf)
	right = mergeSortLinkedList(rightHalf)
	return mergeTheLists(left, right)

def splitList(head):
	slow = fast = head

	if head == None or head.next == None:
		return (head, None)

	while fast.next:
		fast = fast.next
		if fast.next:
			fast = fast.next
			slow = slow.next
	left = head
	right = slow.next
	slow.next = None

	return left, right

def mergeTheLists(left, right):
	fake_head = LinkedList(None)
	curr = fake_head

	while left and right:
		if left.val < right.val:
			curr.next = left
			left = left.next
		else:
			curr.next = right
			right = right.next
		curr = curr.next

	if left == None:
		curr.next = right
	if right == None:
		curr.next = left

	return fake_head.next

if __name__ == '__main__':
	ll = LinkedList(3)
	ll.next = LinkedList(9)
	ll.next.next = LinkedList(100)
	ll.next.next.next = LinkedList(2)
	mergeSortLinkedList(ll)
	display(ll)
