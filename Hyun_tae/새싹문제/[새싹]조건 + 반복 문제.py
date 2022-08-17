#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1330번
a,b=map(int,input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')


# In[7]:


#9498번
a=int(input())
if a>=90:
    print("A")
elif a>=80:
    print("B")
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")


# In[14]:


#14681번
x=int(input())
y=int(input())
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
else:
    print('4')


# In[17]:


#2753번
a=int(input())
if ((a%4==0)and(a%100 !=0)) or (a%400 ==0):
    print('1')
else:
    print('0')


# In[19]:


#2420번
N,M=map(int, input().split())
print(abs(N-M))


# In[26]:


#2741번
a=int(input())
for i in range(1,a+1):
    print(i)


# In[31]:


#10952번
while 1:
    A,B=map(int,input().split())
    if(A==0 and A==0):
        break
    else:
        print(A + B)


# In[33]:


#10872번
n=int(input())
result =1
if n>0:
    for i in range(1,n+1):
        result *= i
print(result)


# In[36]:


#10950번
t=int(input())

for _ in range(t): # t 만큼 반복
    a,b=map(int,input().split())
    print(a+b)


# In[1]:


#10951번
while 1:
    try:
        a,b=map(int,input().split())
    except:
        break
    print(a+b)


# In[3]:


#2739번
n=int(input())

for i in range(1,10):
    print(n,'*',i,'=',n*i)


# In[6]:


#2438번
n=int(input())
for i in range(1,n+1):
    print('*'*i)


# In[ ]:




