class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:           # caso 1: vacía
            self.head = new_node
            self.tail = new_node
        else:                          
            self.tail.next = new_node  
            self.tail = new_node        

        self.size += 1

    def print_all(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(elements))



q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()   # A -> B -> C

