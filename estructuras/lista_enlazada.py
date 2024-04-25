import random

class node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class linkedList:
    def __init__(self):
        self.head=None
    
    def add_at_from(self, data):
        self.head=node(data=data, next=self.head)
    
    def imprime(self):
        nuevo=self.head
        while nuevo:
            print('>>> ', nuevo.data)
            nuevo=nuevo.next
            
    def is_empty(self):
        return self.head==None
    
    def add_at_end(self, data):
        if not self.head:
            self.head=node(data)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node(data=data)
        
    def numeros(self):
        nuevo=self.head
        cp1 = 0
        cp2 = 0
        while nuevo:
            if nuevo.data%2:
                cp1+=nuevo.data
            else:
                cp2+=nuevo.data
            nuevo=nuevo.next
        print(cp1, cp2)
        
    def suma(self):
        nuevo=self.head
        cp = 0
        while nuevo:
            cp += nuevo.data
            nuevo=nuevo.next
        print(cp)
        
    def eliminar(self):
        temp = self.head
        self.head = self.head.next
        temp = None
        if self.head!=None:
            self.head.prev = None
            
            
    def concatenar(self, data):
        if not self.head:
            self.head=node(data)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node(data=data)
    
    def peek(self):
        if self.head is not None:
            print('>>>', self.head.data)
        else:
            print('La pila está vacía')
        
    def is_empty(self):
        return self.head==None


