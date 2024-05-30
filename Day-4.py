
##linear search

l=[1,2,3,4,5,10,99]
key=2
for i in l:
    if i==key:
        print("Found")
        break
else:
    print("not found")

##binary search

l=[1,2,3,4,5]
k=0
i=0
j=len(l)-1
while i<j:
    mid=(i+j)//2
    if l[mid]==k:
        print(mid)
        break
    elif l[mid]<k:
        i=mid+1
    else:
        j=mid-1
else:
    print("not found")

  

##  bubble sort-in each and every iteration the highest/largest number will go to last position.

l=[134,23,8,9,23,56]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)        



##in selection smallest number will go first
##first value will be taken as min value and stored in m variable
##i will start at first and j will start from i+1

l=[2,4,11,5,6,1]
for i in range(len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if  l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)



## in insertion sort we will insert in the position where it belongs to
# i will start from second position as first is always sorted(sorted order)
# j will start from i-1(unsorted order)

l=[33,2,22,45,12,999,667]
for i in range(1,len(l)):
    m=l[i]
    j=i-1
    while j>-1 and l[j]>m:
        l[j+1]=l[j]
        j-=1
    l[j+1]=m
print(l)



##quick sort -somewhat like insertion sort 
#pivot element as first element
#i will be pivot +1 and j will be last position

l=[33,444,2222,7777,44,55,22]
def partition(l,beg,end):
    pi=l[beg]
    start=beg+1
    stop=end
    while True:
        while start<len(l) and l[start]<pi:
            start+=1
        while stop>-1 and l[stop]>pi:
            stop-=1
        if start<stop:
            l[start],l[stop]=l[stop],l[start]
        else:
            break
    l[beg],l[stop]=l[stop],l[beg]
    return stop
def quick(l,i,j):
    if i<j:
        p=partition(l,i,j)
        quick(l,i,p-1)
        quick(l,p+1,j)
quick(l,0,len(l)-1)    
print(l)


##creation of node in tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Trees:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newnode=Node(value)
        if not self.root:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data>value:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
                    
    def preorder(self):
        self.helper(self.root)
    def helper(self,root):
        if root:
            print(root.data)
            self.helper(root.left)
            self.helper(root.right)
t=Trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(1)
t.insert(7)
t.insert(6)
t.insert(8)
t.preorder()

 
## post order

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Trees:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newnode=Node(value)
        if not self.root:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data>value:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
    def preorder(self):
        self.helper(self.root)
    def helper(self,root):
        if root:
            print(root.data)
            self.helper(root.left)
            self.helper(root.right)
t=Trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(1)
t.insert(7)
t.insert(6)
t.insert(8)
t.preorder()
