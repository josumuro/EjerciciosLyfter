class node:
 def __init__(self,value):
  self.value=value
  self.next=None

class Stack:
 def __init__(self):
  self.top= None
  self.size=0


 def push(self,value):
  new_node=node(value)
  new_node.next=self.top
  self.top=new_node
  self.size += 1

def pop(self):
 if self.size==0:
  return None
 else:
  value=self.top.value
  self.top=self.top.next
  self.size -= 1
  return value
 
def peek(self):
 if self.size==0:
  return None
 else:
  return self.top.value
 
def is_empty(self):
 return self.size==0

def get_size(self):
 return self.size

print(100*"-")