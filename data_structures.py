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
class SLNode: # first node in a list is the head
    def __init__(self, value):
        self.value = value # whatever the value of the node is for each node
        self.next = None # the link to the next node in the list, or set to None if no next node

# The list should also have some functionality
class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val): # add a value to the front of the list
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self): # print out the values in the list
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val): # add an value to the end of a list
        if self.head == None:	# if the list is empty, add to front!
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self): # remove the first node and return it's value
        pass

    def remove_from_back(self):
        pass

    def remove_value(self, value):
        pass

    def insert_at(self, value, n):
        pass

# New list example
my_list = SList() # create the list
my_list.add_to_front("d") # "d"
my_list.add_to_front("c") # "c->d"
my_list.add_to_front("b") # "b->c->d"
my_list.add_to_front("a") # populate list, final order "a->b->c->d"
my_list.print_values()