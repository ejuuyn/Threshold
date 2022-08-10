#!/usr/bin/env python
# coding: utf-8

# In[2]:


#15552번
import sys
t=int(sys.stdin.readline())

for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)


# In[6]:


#10871번
n,x = map(int, input().split())
num=list(map(int, input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end = " ")


# In[7]:


#10807번
n=int(input())
data=list(map(int,input().split()))

v=int(input())
print(data.count(v))


# In[9]:


#5597번
a=[i for i in range(1,31)]
for _ in range(28):
    a.remove(int(input()))
print(*a,sep="\n")


# In[10]:


#2738번
n,m=map(int, input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
for row in matrix:
    sec_row = list(map(int, input().split()))
    for i in range(m):
        row[i] += sec_row[i]
        print(row[i], end = '')
        print()


# In[11]:


#11654번
a=input()

print(ord(a))


# In[12]:


#2743번
print(len(input()))


# In[13]:


#2744번
a=input()
print(a.swapcase())


# In[25]:


#2754번
a={'a+':4.3, 'a0':4.0, 'a-': 3.7, 'b+':3.3,'b0': 3.0,'b-':2.7, 'c+':2.3, 'c0':2.0, 'c-':1.7, 'd+':1.3,'d0': 1.3, 'd-':1.0, 'f':0.0}
n=input()
print(a[n])


# In[28]:


#10809번
a=input()
alphabet=list(range(97,123))
for x in alphabet:
    print(a.find(chr(x)))


# In[29]:


#11718번
while True:
    try:
        print(input())
    except EOFError:
        break


# In[ ]:


#9086번
for _ in range(int(input())):
    string = input()
    print(string[0], string[-1], sep='')


# In[1]:


n=int(input())

a=[0,1]
for i in range(2, n+1):
    num=a[i-1] + a[i-2]
    a.append(num)
print(a[n])


# In[3]:


#15964번
a,b=map(int, input().split())
print((a+b)*(a-b))


# In[5]:


#2475번
data=list(map(int,input().split()))
result = 0
for i in range(len(data)):
    result += (data[i]**2)
    
print(result%10)


# In[ ]:




