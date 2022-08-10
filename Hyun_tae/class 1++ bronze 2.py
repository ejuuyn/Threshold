#!/usr/bin/env python
# coding: utf-8

# In[3]:


#2884  시간 알람 설정하기
h,m=map(int,input().split())
if m>=45:
    print(h,m-45)
elif h>0 and m<45:
    print(h-1,m+15)
else: #24시간 기준이니 0시일 경우엔 23시로 표기해야함
    print(23,m+15)


# In[4]:


#2908번 #상수 출력하기
a,b=input().split() #입력받은 숫자는 역순으로 재배치해야하기 때문에 역순으로 재배치한 후 숫자로 변환하였다
a=int(a[::-1]) #[::-1]은 역순을 의미한다
b=int(b[::-1]) #숫자는 분리해서 사용할 수 없기 때문에 역순으로 변환한 후 숫자로 변환했다

if a>b:
    print(a)
else:
    print(b)


# In[5]:


#2920번 #숫자를 지정된 알파벳으로 치환하기
a = list(map(int,input().split())) #list로 값 입력

if a == sorted(a): #sorted()함수는 오름차순 또는 내림차순으로 값 변환 #리스트명만 있으면 오름차순
    print('ascending')
elif a== sorted(a,reverse=True): #reverse값이 True면 내림차순
    print('descending')
else:
    print('mixed')


# In[8]:


#3052번 
n=[] #n을 list로 선정

for _ in range(10): #10번 반복=0부터 9까지 반복
    a=int(input()) #숫자 입력받고
    b=a%42 #42로 나눠준다
    n.append(b) #나눠준 값을 리스트에 넣는다

s = set(n) #중복제거 필터 역할 #리스트에 넣은 값 중복제거
print(len(s)) #최종값 출력


# In[ ]:


#8958번
t=int(input()) #테스트 케이스 개수 입력

for _ in range(t):
    a=list(input())
    


# In[ ]:


#10818번 최소 최대값
n=int(input())
a=list(map(int,input().split()))


# In[ ]:


#11720번
n=int(input())

for _ in range(n):
    a=int(input())
    

