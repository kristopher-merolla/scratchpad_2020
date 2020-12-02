####################################
## -- Notes on Data Structures -- ##
####################################

# Info on bits and bytes https://web.stanford.edu/class/cs101/bits-bytes.html
# 1 byte = 256 bits (2^8)
# 1 kb = 1000 bytes
# 1 mb = 1000000 bytes
# 1 gb = 1000 mb

# Complexity and Big-O Notation
# O(N)
# log(N)
# O(N^2)
# O(N^3)

# Linked List
# a->b->c->d

# a, b, c, and d above are nodes which is a class that has two attributes:
class SLNode:
    def __init__(self, value):
        self.value = value # whatever the value of the node is for each node
        self.next = None # the link to the next node in the list, or set to None if no next node

# First node in a list is the head
class SList:
    def __init__(self):
    	self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        new_node.next = self.head
        self.head = new_node

# New list example
my_list = SList() # create the list
# populate list, in order "a->b->c->d"
my_list.add_to_front("d")
my_list.add_to_front("c")
my_list.add_to_front("b")
my_list.add_to_front("a")