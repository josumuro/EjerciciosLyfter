class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # pointer to the front of the queue
        self.rear = None 
        self.size=0

    def enqueue(self,value):
        new_node= Node(value)  # create a new node with the given value
        if  self.rear is None:  # if the queue is empty
            self.front = new_node  # set both front and rear to the new node
            self.rear = new_node
        else:
            self.rear.next = new_node  
            self.rear = new_node  

    def dequeue(self):
        if self.front is None: 
           return None
        dequeued_node= self.front 
        self.front= self.front.next  

        if self.front is None:  
            self.rear = None  

        return dequeued_node.value  
    def print_all(self):
     if self.front is None:
        print("Queue vacía")
        return

     current = self.front            
     elements = []

     while current:                 
        elements.append(current.value)
        current = current.next     

     print(" -> ".join(elements))   
    
q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()
    