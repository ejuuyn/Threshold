#!/usr/bin/env python
# coding: utf-8

# #2884번 알람 시계

# In[7]:


H,M=map(int,input().split())

reM=M-45

if reM<0:
    H=H-1
    if H==-1:
        H=23
    M=60+reM
    print(H,M)
else:
    print(H,reM)


# #2908번 상수

# In[13]:


n1,n2=map(int,input().split())

rev1=[]
rev2=[]
rev1a=[]
rev2a=[]
for i in str(n1):
    rev1.append(i)
for i in range(1,len(rev1)+1):
    rev1a.append(rev1[-i])
for i in str(n2):
    rev2.append(i)
for i in range(1,len(rev2)+1):
    rev2a.append(rev2[-i])

if int("".join(rev1a))>int("".join(rev2a)):
    print("".join(rev1a))
else:
    print("".join(rev2a))


# #2920번 음계

# In[19]:


da=[1,2,3,4,5,6,7,8]
melody=list(map(int,input().split()))

if melody==sorted(da):
    print("ascending")
elif melody==sorted(da,reverse=True):
    print('descending')
else:
    print('mixed')


# # 3052번 나머지

# In[24]:


a=[]
for i in range(10):
    a.append(int(input()))

s=set()
for i in a:
    s.add(i%42)
print(len(s))


# # 8958번 ox퀴즈

# In[9]:


case=int(input())
score=[]
print_score=[]
s=0
for i in range(case):
    test=input().upper()
    for j in test:              #이중 반복
        if j=='O':
            s+=1
        else:
            s=0
        score.append(s)          #j가 O이면 스코어+1 X면 zero로 score 리스트에 추가
    s=0                          #print_score리스트에 score합 추가 후 score리스트 초기화  
    print_score.append(sum(score))
    score=[]
for i in range(case):
    print(print_score[i])


# # 9498번 시험 성적

# In[15]:


score=int(input())
if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('F')


# # 10172 dog

# In[24]:


print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')


# # 10809 alphabet

# In[40]:


s=input()
alpha='abcdefghijklmnopqrstuvwyxz'
for i in alpha:
    print(s.find(i),end=' ')


# # 10808 최소 최대

# In[43]:


N=int(input())
a=list(map(int,input().split()))

print(min(a),max(a))


# # 10869 사칙연산

# In[45]:


a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)


# # 10871번 X보다 작은 수

# In[52]:


n,x=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if a[i]<x:
        b.append(str(a[i]))
print(" ".join(b))    


# # 10950 a+b

# In[ ]:


t=int(input())
sumab=[]
for i in range(t):
    a,b=map(int,input().split())
    sumab.append(a+b)
for i in range(len(sumab)):
    print(sumab[i])


# In[2]:


while True:
    a,b=map(int,input().split())    
    if a==0 and b==0:
        break
    print(a+b)


# In[3]:


a,b=map(int,input().split())
print(a*b)


# # 아스키 코드

# In[6]:


m=input()
print(ord(m))


# # 11720 숫자의 합

# In[14]:


n=int(input())
s=input()
s_list=[]
for i in range(n):
    s_list.append(int(s[i]))
print(sum(s_list))    


# In[ ]:




