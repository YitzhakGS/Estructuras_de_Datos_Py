class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def inserta_Frente(self, data):
        vtx = node(data)
        vtx.next = self.head
        vtx.prev = None
        
        if self.head != None:
            self.head.prev = vtx
        
        self.head = vtx
        
        if self.tail == None:
            self.tail = vtx
    
    def imprime(self):
        actual = self.head
        while actual:
            print(actual.data, end=" <--> ")
            actual = actual.next
        print("None")
        
    def imprime_atras(self):
        actual = self.tail
        while actual:
            print(actual.data, end=" <--> ")
            actual = actual.prev
        print("None")
        
    def inserta_Atras(self, data):
        if not self.head:
            self.head=node(data)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node(data=data)
        
    def insertar_entre(self, data, i):
        if self.head is not None:
            curr = self.head
            for k in range(i-1):
                curr = curr.next
            aft = curr.next
            vtx = node(data)
            vtx.next = aft
            aft.prev = vtx
            curr.next = vtx
            vtx.prev = curr
            
    def eliminar_i(self):
        temp = self.head
        self.head = self.head.next
        temp = None
        if self.head!=None:
            self.head.prev = None
            
    def eliminar_f(self):
        if self.tail is not None:
            self.tail.prev = self.tail
            if self.tail!=None:
                self.tail.next = None
                
    def eliminar_e(self, i):
        if self.head is not None:
            curr = self.head
            for k in range(i-1):
                curr = curr.next
            delete = curr.next
            aft = delete.next
            curr.next = aft
            aft.prev = curr
            del delete
            
        
        
dll = Double_Linked()
dll.inserta_Atras(22)
dll.inserta_Frente(4)
dll.inserta_Frente(5)
dll.inserta_Frente(42)
dll.inserta_Frente(23)
dll.inserta_Frente(55)
dll.inserta_Frente(77)
dll.imprime()
dll.insertar_entre(3, 2)
dll.imprime()
dll.eliminar_i()
dll.imprime()
dll.eliminar_f()
dll.imprime()
dll.eliminar_e(2)
dll.imprime()
