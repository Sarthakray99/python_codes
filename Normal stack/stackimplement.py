class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # inserts a new element to the top of the stack
        self.items.append(item)

    def pop(self):  # gives the top most element by popping it by using the built-in pop function
        self.items.pop()

    def is_empty(self):
        return self.items == []  # returns true if stack is empty orelse false

    def peek(self):
        if not self.is_empty():
            print(self.items[-1])
        else:
            print(self.get_stack())

    def get_stack(self):
        return self.items


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_stack())
print(s.is_empty())
s.peek()