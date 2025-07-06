class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
            self.tail=new_node

    

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head:
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=new_node
            self.tail=new_node

    
    def remove_from_beginning(self):
        if not self.head:
           return "Linked list is empty."
        
        if self.head == self.tail:
           self.head = None
           self.tail = None
        else:
           self.head = self.head.next

    def remove_from_end(self):
        if not self.head:
            return "empty linked list"
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            current=self.head
            while current.next!=self.tail:
                current=current.next
            self.tail=current
            current.next=None        

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next

        print("None")           
    
    
    def insert_at(self,index):
        pass
    
    
    def search(self,data):
        pass

    def remove_from(self,index):
        pass

ll = LinkedList()


ll.insert_at_beginning(20)
ll.display()

ll.insert_at_end(30)
ll.display()

ll.insert_at_beginning(80)
ll.insert_at_beginning(100)
ll.insert_at_beginning(190)
ll.insert_at_beginning(99)
ll.display()

ll.remove_from_beginning()
ll.remove_from_end()
ll.display()