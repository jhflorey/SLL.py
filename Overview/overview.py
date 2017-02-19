#Demonstration - reversing the array:

# Swap the first and the last value in the array  (e.g. [1,3,2,4,5,7] => [7,3,2,4,5,1])
x = [5,2,3,6,1,12]
x[0], x[-1] = x[-1], x[0]
print x

# Swap the second and the second to last value in the array (e.g. [7,3,2,4,5,1] => [7,5,2,4,3,1])
x = [7,3,2,4,5,1]
x[1], x[-2] = x[-2], x[1]
print x

# Do this until we swap the two values in the middle (e.g. [7,3,4,2,5,1] => [7,5,4,2,3,1])
x = [7,3,4,2,5,1]
x[1], x[-2] = x[-2], x[1]
print x
x[2], x[-3] = x[-3], x[2]
print x

# Demonstration - Removing the last node in the Doubly LinkedList
# A node of the doubly linked List
class Node(object):
	# to create a new node:
	def __init__(self, data, prev, next):
		self.data = data
		self.next = next
		self.prev = prev

class DLL(object):

	head = None
	tail = None

	def append(self, data):
		new_node = Node(data, None, None)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.prev = self.tail
			new_node.next = None
			self.tail.next = new_node
			self.tail = new_node

	def remove(self, node_value):
		current_node = self.head

		while current_node is not None:
			if current_node.data == node_value:
				# if it's not the first element
				if current_node.pre is not None:
					current_node.prev.next = current_node.next
					current_node.next.prev = current_node.prev
				else:
					# otherwise we have no prev (it's None), head is the next one, and prev becomes None
					self.head = current_node.next
					current_node.next.prev = None

			current_node = current_node.next

	def show(self):
		print "show list data:"
		current_node = self.head
		while current_node is not None:
			print current_node.prev.data if hasattr(current_node.prev, "data") else None,
			print current_node.data,
			print current_node.next.data if hasattr(current_node.next, "data") else None,

			current_node = current_node.next
		print "*"*50


d = DLL()
 
d.append(5)
d.append(6)
d.append(50)
d.append(30)
 
d.show()
 
d.remove(50)
d.remove(5)
 
d.show()



	







