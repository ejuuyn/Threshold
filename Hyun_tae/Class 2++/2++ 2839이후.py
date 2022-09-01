#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2839
s=int(input())

b=0
while s>=0:
    if s % 5 ==0:#5의 배수일 때 - 컴활 엑셀에서 본 구문이다
        b+=(s//5)
        print(b)
        break
    s-=3
    b+=1
else:
    print(-1)


# In[ ]:


#2869


# In[ ]:


#4153
while True:
    n=list(map(int,input().split()))
    if sum(n) ==0: #마지막 줄에 0 0 0입력되면서 끝나야하니까
        break #break로 끝내기
    max_n = max(n) #max_n에다가 입력받은 수 중 가장 큰 수 넣기
    n.remove(max_n) #제일 큰 수를 리스트에서 삭제시킨다, 세 수는 오름차순으로 되기 않아 제일 큰게 어딨는지 모른다. 그래서 빼고 계산
    if n[0]**2 + n[1]**2 == max_n**2: #**=제곱
        print('right')
    else:
        print('wrong')


# In[ ]:


#4949
while True:
    s=input()
    


# In[ ]:


#7568
n= int(input())

data = [] # 입력
a = [] # 등수
for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y)) # 몸무계와 키를 묶어서 append 해줌
 
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: 
            count += 1 
    ans.append(count + 1) 
 
for d in a:
    print(d,end=" ")


# In[ ]:


#9012


# In[ ]:


#10250


# In[ ]:


#10773
k = int(input())
z = []
for i in range(k):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))


# In[ ]:


#10814


# In[ ]:


#10816
import sys #이거 진짜 모르겠다

