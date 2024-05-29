# ## creation of linked list 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(6)
c=node(7)
d=node(8)
a.next=b
b.next=c
c.next=d
print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)

##in other way
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
            self.head==newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
a=linkedlist()    
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)     

##

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
            self.head==newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
def printlist(self):
    curr=self.head
    while curr:
        print(curr.data,end="->") 
        curr=curr.next
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)

##

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
           self.head==newnode
           return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head    #for traversing
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
a=linkedlist()    
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)
print(a.head.next.next.next.data)
print(a.head.next.next.next.next.data)


##

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
           self.head==newnode
           return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head    #for traversing
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
a=linkedlist()    
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.delatbeg()
a.delatend()
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)


###count

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
           self.head==newnode
           return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head    #for traversing
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def count(self):
        c=1
        curr=self.head    #if head is not none then it will only run
        while curr.next:
            c+=1
            curr=curr.next
        print(c)
    
a=linkedlist()    
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.delatbeg()
a.delatend()
a.count()
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)

##search
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
           self.head==newnode
           return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head    #for traversing
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def count(self):
        c=1
        curr=self.head    #if head is not none then it will only run
        while curr.next:
            c+=1
            curr=curr.next
        print(c)
    def search(self,value):
        curr=self.head    #for traversing
        while curr:
            if curr.data==value:
                print("yes")
                break
            curr=curr.next
        else:
            print("no")
    
a=linkedlist()    
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.delatbeg()
a.delatend()
a.count()
a.search(7)
print(a.head.data)    
print(a.head.next.data)   
print(a.head.next.next.data)


###

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None      
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==node:
           self.head==newnode
           return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head    #for traversing
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def count(self):
        c=1
        curr=self.head
        while curr.next:
            c+=1
            curr=curr.next
        print(c)
        m=c//2
        i=0
        curr=self.head
        while i!=m:
            curr=curr.head
            i+=1
        print(curr.data)
    def search(self,value):
        curr=self.head    #for traversing
        while curr:
            if curr.data==value:
                print("yes")
                break
            curr=curr.next
        else:
            print("no")
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2) 
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.delatbeg()
a.delatend()
a.count()
print(a.head.data)
print(a.head.next.data)
print(a.head.next.next.data)
