class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def push_right(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.left = self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        self.size += 1

    def push_left(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.left = self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        self.size += 1

    def pop_right(self):
        if self.size == 0:
            raise IndexError("Deque vacío")
        value = self.right.value
        if self.size == 1:
            self.left = self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None
        self.size -= 1
        return value

    def pop_left(self):
        if self.size == 0:
            raise IndexError("Deque vacío")
        value = self.left.value
        if self.size == 1:
            self.left = self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        self.size -= 1
        return value

    def __repr__(self):
        elements = []
        current = self.left
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"[LEFT] {' ↔ '.join(elements)} [RIGHT]"



d = Deque()

d.push_right(10)
d.push_right(20)
d.push_right(30)
print(d)              

d.push_left(5)
print(d)            
print(d.pop_right())  
print(d.pop_left())   
print(d)              