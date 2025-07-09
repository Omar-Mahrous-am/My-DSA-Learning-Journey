class Node :
    def __init__(self,data):
        self.data=data
        self.next=None



class queue:

   
    def __init__(self):
        self.head=None
        self.tail=None

    
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.tail:
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=new_node
            self.tail=new_node

  
  
    def dequeue(self):
        if self.head:
            current_node=self.head
            self.head=current_node.next
            if self.head==None:
                self.tail=None
            current_node.next=None
            return current_node.data
        else:
            self.tail=None
            return None
        
   
   
    def isempty(self):
        if self.head:
            return True
        else:
            return False



