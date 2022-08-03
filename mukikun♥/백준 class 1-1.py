#!/usr/bin/env python
# coding: utf-8

# #A/B 1008번

# In[5]:


a,b=input().split()
A=int(a)
B=int(b)

print(A/B)


# #단어의 개수 1152번

# In[ ]:


b=str(input())
s=b.split()
print(len(s))


# #1157번 단어공부

# In[27]:


a=list(set(input().upper()))  #missisipi -> [M','I','S','P']
count=[]

for i in a:
    c=a.count(i)  #M
    count.append(c)

if count.count(max(count))>=2:
    print('?')
else:
    print(max(a,key=a.count))


# In[31]:


a=input().upper()      #입력받은 문자열 대문자로 치환 ex)missisipi-> MISSISIPI
a_list=list(set(a))    #같은 문자간 중복을 피하기 위해 집합으로 만들고 count함수를 쓰기위해 다시 리스트로 ex)MISSISIPI->['M','I','S','P']
                       #집합으로 안할 시에 MISSISIPI를 반복하면 밑에서 [1,4,3,3,4,3,4,1,4]로 리스트가 형성됨  
c=[]

for i in a_list:
    count=a.count(i)   #리스트 원소 수만큼만 반복해서 원래 문자열에 원소 개수 찾기
    c.append(count)    

if c.count(max(c))>=2:  #가장 높은 수가 중복되는지 확인
    print('?')
else:
    print(max(a,key=a.count))


# #1330번 두 수 비교하기

# In[ ]:


a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    print(">")
elif a<b:
    print('<')
else:
    print('==') 
#이거 도대체 왜 틀린거임?
도대체 뭐냐구/..


# #2438번 별 찍기

# In[15]:


a=int(input())
for i in range(1,a+1):
    print("*"*i)


# #2439번 별찍기2

# In[20]:


a=int(input())
for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)


# #2475번 검증 수

# In[6]:


a1,a2,a3,a4,a5=map(int,input().split())

k=(a1**2+a2**2+a3**2+a4**2+a5**2)%10
print(k)


# #1546번 평균

# In[36]:


N=int(input())
a=list(map(int,input().split()))
a_max=max(a)

for i in range(len(a)):
    a[i]=a[i]/a_max*100
    
print(sum(a)/N)


# #2562번 최댓값

# In[41]:


a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)


# #2577 숫자의 개수

# In[49]:


A=int(input())
B=int(input())
C=int(input())

mul=A*B*C
mul_list=[]
for i in str(mul):
    mul_list.append(i)
print(mul_list.count('0'))
print(mul_list.count('1'))
print(mul_list.count('2'))
print(mul_list.count('3'))
print(mul_list.count('4'))
print(mul_list.count('5'))
print(mul_list.count('6'))
print(mul_list.count('7'))
print(mul_list.count('8'))
print(mul_list.count('9'))


# #2739번 구구단

# In[50]:


N=int(input())
for i in range(1,10):
    print(N,"*",i,"=",N*i)


# #2741번 N 찍기

# In[51]:


N=int(input())
for i in range(1,N+1):
    print(i)


# #2675번 문자열 반복

# In[73]:


R,S=map(str,input().split())
R=int(R)

S_list=[]
for i in S:
    S_list.append(i*R)
print("".join(S_list))


# #2753번 윤년

# In[63]:


N=int(input())
if N%4==0 and N%400==0 or N%100!=0:
    print(1)
else:
    print(0)


# #2742번 기찍 N

# In[64]:


N=int(input())
for i in range(N):
    print(N-i)


# In[ ]:




