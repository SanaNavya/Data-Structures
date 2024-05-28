## attributes class and object example

# class student:
#     roll=34
#     sec=33
#     def study(self):
#         print("study")
# rahul=student()
# rahul.study()


##basic constructor example using encapsulation

# class student:
#     def __init__(self,roll,sec):
#         self.roll=roll
#         self.sec=sec
#     def study(self):
#         print("i study and my roll call is ",self.roll)    
# rahul=student(12,"a")
# rahul.study()
# bijen=student(13,"b")
# bijen.study()

## stack

# l=[1,2,3,4]
# def app(val):
#     l.append(val)
# def p():
#     l.pop()
# app(5)
# p()
# print(l)        

## stack using class function

##class stack:
#     def __init__(self):
#         self.l=[]
#     def push(self,data):
#         self.l.append(data) 
#     def pop(self):
#         self.l.pop()  #put 0 to make queue function
#     def peek(self):
#         print(self.l[-1])    
# s=stack()
# s.push(1)
# s.push(2)
# s.push(3) 
# s.pop()
# print(s.l)
# s.peek()  


## postfix expression


s="5678+-*"
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
    elif i=="+":
        a=st.pop()
        b=st.pop()
        st.append(a+b)
    elif i=="-":
        a=st.pop()
        b=st.pop()
        st.append(a-b)
    elif i=="*":
        a=st.pop()
        b=st.pop()
        st.append(a*b)
    elif i=="/":
        a=st.pop()
        b=st.pop()
        st.append(a/b)
    elif i=="%":
        a=st.pop()
        b=st.pop()
        st.append(a%b)
print(st[0])                       

    
