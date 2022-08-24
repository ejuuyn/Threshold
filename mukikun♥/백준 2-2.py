#!/usr/bin/env python
# coding: utf-8

# # 2164번 카드2

# In[2]:


'''
n장의 카드 1부터 n까지
버리고 밑으로 버리고 밑으로
리스트활용해서 pop쓰면 될듯?
problem1.li2의 순서
2.
'''
import time
n=int(input())
start=time.time()
li=[]
li2=[]
for i in range(n,0,-1):
    li.append(i)
for _ in range(n-1):
    while len(li)!=0:
        li.sort(reverse=True)
        li.pop()
        if len(li)!=0:
            li2.append(li.pop())
        else:
            break
    if len(li)+len(li2)==1:
        break
    while len(li2)!=0:
        li2.sort(reverse=True)
        li2.pop()
        if len(li2)!=0:
            li.append(li2.pop())
        else:
            break
    if len(li)+len(li2)==1:
        break

end=time.time()
try:
    print(li[0])
except:
    print(li2[0])
print(end-start)


# In[65]:


n=int(input())
li=[]
for i in range(1,n+1):
    li.append(i)
for i in range(n-1):
    del li[0]
    li.append(li.pop(0))
print(li[0]) 


# # 2231번 분해합

# In[ ]:


'''
자연수 N, 분해합M의 생성자
가장 작은 생성자를 구하는 프로그램
흠..숫자를 다 훑는 수밖에 없나
생각
1.반복으로 숫자들의 모든 분해합을 구한다.
2.반복 범위는 N/2~N
3.N과 분해합이 맞으면 리스트로 넣고 min
뭐고 어캐맞았누
'''
N=int(input())
create=[]
i_list=[]
for i in range(N//2,N):
    j_list=[]
    j_list.append(i)
    for j in range(len(str(i))):
        j_list.append(int(str(i)[j]))
    if sum(j_list)==N:
        i_list.append(i)
try:
    print(min(i_list))
except:
    print(0)


# # 2292번 벌집

# In[ ]:


'''
이..뭔..
테두리가 등차수열로 올라감 N+6 
6 12 18 24
6 18 36 60...이 수열 뭐라고 하더라
생각
6 18 36
6*1 6*3 6*6 6*10 6*15...6*(i*(i+1)/2)
n-1을 6*(i*(i+1)/2)로 나눠서 올림 해버리면 i+1개를 최소거리로 가질 듯
시간초과 썅
반복 2만번도 안하는데 왜 시간초과죠
에라이
심지어 여기서 2초 안걸림;
'''
def up(x):
    if int(x)<x<int(x)+1:
        x=int(x)+1
        return x
    else:
        return int(x)

n=int(input())

for i in range(1,n//2):          #틀림
    if up((n-1)/(6*(i*(i+1)/2)))!=1:
        continue
    else:
        print(i+1)
        break     

while up((n-1)/(6*(i*(i+1)/2)))!=1: #시간초과
    i+=1
print(i+1)


# # 2609번 최대공약수와 최소공배수

# In[9]:


'''
두 자연수의 최대공약수와 최소공배수
생각
1.최대공약수
-for문으로 1부터 훑으며 두 수의 약수인지 확인 and문
-제일 큰 공약수가 최대공약수
2.최소공배수
-공약수 리스트 다 곱하면 되나 x
각 수를 최대 공약수로 나눈 몫을 다 곱하면? 해보자
'''
m,n=map(int,input().split())

for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
        k=i
        
print(k)
print(int(k*(m/k)*(n/k)))


# # 2751번 수 정렬하기

# In[3]:


'''
리스트로 정렬하고
출력하면
'''
n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
li.sort()
for i in range(n):
    print(li[i])


# # 2775번 부녀회장이 될거야

# In[37]:


'''
a층 b호에 사는 사람 수 a-1(1)+a-1(2)+...+a-1(b)
0층에 사는 사람
1 2 3 4 5 6 7 8...
1층에 사는 사람
1 3 6 10 15 21 
note'''
def combination(n,r):
    x=1
    y=1
    for i in range(r):
        x=x*(n-i)
        y=y*(i+1)
    return x/y

t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    print(int(combination(n+k,k+1)))


# # 2798번 블랙잭

# In[40]:


'''
서로 다른카드?
모든 3원소합 경우의 수를 구해서 m과의 차가 최소가 되는 점을 찾으면 될듯
틀렸네
'''
n,m=map(int,input().split())
li=list(map(int,input().split()))
li2=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and i!=k and j!=k:
                li2.append(li[i]+li[j]+li[k])
li3=[]
for i in li2:
    li3.append(abs(m-i))
mini=min(li3)
print(li2[li3.index(mini)])


# # 2805번 나무자르기

# In[41]:


'''
sum(나무의 높이-H)=M(가져갈 길이)
H의 최댓값 구하기
숫자 개큼->이분탐색
H가 0부터 제일 높은 나무의 길이 사이 어딘가에 있음
그 중에서 m을 만족하는 최댓값을 찾으려면?
'''
n,m=map(int,input().split())
height=list(map(int,input().split()))
start,end=0,sum(height)

while start<=end:
    mid=(start+end)//2
    h=0
    for i in height:
        if i>mid:
            h+=i-mid
    if h>=m:
        start=mid+1
    else:
        end=mid-1
print(end)


# # 2839번 설탕 배달

# In[50]:


'''
3키로 5키로 설탕봉지
최소값
먼저 5키로로 N을 나누고 나머지가 0 혹은 3의 배수이면 출력
아니면 -1 출력하면 될듯
3으로 나누고 나머지가 5의 배수인 경우를 어떻게 표현해야하지
'''
def integer(x,y,k):
    x,y=1
    if k==3x+5y:
        return x+y
    else:
        
N=int(input())
m=N%5
l=N%3
if m==0:
    print(N//5)
elif m%3==0:
    print(N//5+m//3)
elif l==0:
    print(N//3)
else:
    print(-1)


# In[ ]:




