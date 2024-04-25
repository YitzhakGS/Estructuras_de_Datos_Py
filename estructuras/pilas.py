
class node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class Pila:
    def __init__(self):
        self.head=None
    
    def push(self, data):
        vtx = node(data)
        vtx.next = self.head
        vtx.prev = None
        
        self.head = vtx
    
    def peek(self):
        if self.head is not None:
            print('>>>', self.head.data)
        else:
            print('La pila está vacía')
            
    def pop(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
            
    def is_empty(self):
        return self.head==None
    


