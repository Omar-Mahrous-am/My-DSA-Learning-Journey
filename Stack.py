class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    
    
    def push(self,data):
        new_node=Node(data)
        if self.top:
            new_node.next=self.top
            
        self.top=new_node
    def pop(self):
        if self.top:
            popped_node=self.top
            self.top=self.top.next
            return popped_node.data
        else:
            return None
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
