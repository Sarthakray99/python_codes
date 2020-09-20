class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):  # function to insert new elements into the linked list || Adding a node to the end of the list
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head  # we set it to first when the list is created and then we move it thr=ugh the llist until we get null so eventually last_node will actually point to the last node
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  # we insert a new node here

    def prepend(self, data):  # Adding a node to the beginning of the list
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None
        


llist = LinkedList()
'''
n = int(input("Enter the number of data you want to enter"))
for i in range(n):
    l = input("Enter data")
    list1.append(l)
'''
llist.append("Lemon")
llist.append("Water")
llist.append("Is")
llist.append("Nice")

llist.insert_after_node(llist.head.next, "Not")  # it takes the node containing the data element b or if you want any other node you can loop through and find the .next value and pass it as an argument to this function

llist.print_list()