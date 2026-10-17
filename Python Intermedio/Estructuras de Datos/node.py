class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.size == 0:
            return None
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def print_all(self):
        if self.top is None:
            print("Stack vacío")
            return
        current = self.top
        while current:
            print(current.value)
            current = current.next




s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.print_all()

print(s.pop())
s.print_all()

