class node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class deq:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def Enq(self, data):
        if not self.head:
            self.head=node(data)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node(data=data)
        
    
    def imprime(self):
        nuevo=self.head
        while nuevo:
            print('>>> ', nuevo.data)
            nuevo=nuevo.next
            
    def Deq(self):
        temp = self.head
        self.head = self.head.next
        temp = None
        if self.head!=None:
            self.head.prev = None
        
            
    def is_empty(self):
        return self.head==None
    
    def peek_front(self):
        if self.head is not None:
            print('>>>', self.head.data)
        else:
            print('La pila está vacía')



