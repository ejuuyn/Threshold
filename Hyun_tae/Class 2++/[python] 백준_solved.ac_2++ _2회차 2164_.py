#!/usr/bin/env python
# coding: utf-8

# In[4]:


#2164번 카드2 큐를 이용한 문제
#deque: 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다
#deque관련 블로그 https://dongdongfather.tistory.com/72


from collections import deque

n=int(input())
q=deque()
for i in range(1,n+1): #q에 1부터 n까지 넣어주기
    q.append(i)

while len(q) >1:
    q.popleft() #제일 위 카드 버리기
    q.append(q.popleft()) #제일 위 카드 바닥으로 옮기기

print(q.pop())


# In[14]:


#2164-deque연습하기
#https://dongdongfather.tistory.com/72 참고

from collections import deque
dq=deque('love')
dq

dq.append('m') # dq 맨 뒤에 m 추가하기 그러면 l o v e m 이 된다
dq.pop() #pop을 통해 맨 오른쪽 끝에 항목 가져오면서 삭제함 그러면 다시 l o v e가 된다 pop! 나간다

#그러면 맨 처음(왼쪽)에 넣고 싶을땐? appendleft
dq.appendleft('l') #왼쪽에서 i 입력 그러면 l l o v e가 된다
dq.popleft() #맨 처음(왼쪽)을 뽑고 싶을땐 popleft()


# In[3]:


#2331번 분해합 구하기
#분해합은 어떤 자연수 N이 있을 때, 자연수 N과 N의 각 자리수와 합을 의미한다 ex)245(245+2+4+5=256)
#생성자 M의 분해합이 N = M은 N의 생성자
#자연수 N이 주어졌을 때 가장 작은 생성자를 구하는 프로그램

#부르트 포스
#조합 가능한 모든 경우를 하나씩 대입하는 방법 = 완전탐색

n=int(input()) #입력값 받기
result=0 #결과를 담을 변수를 생성

for i in range(1,n+1): #for문으로 1부터 n까지 모든 수를 계산해보며 분해합 계산 = 완전탐색 = 부르트 포스
    a=list(map(int, str(i))) #str함수로 i의 각 자리수를 a리스트에 넣기 #str로 각 자리수(i의 자리수)를 문자로 뽑은 후 int로 숫자처리
    result= i + sum(a) #그대로인 값 i와 각 자리수가 들어간 a리스트의 합을 더하면 된다
    if result == n: #답과 입력값(n)을 비교한다 같으면 i 출력하기 # 제일 작은 수를 출력하라는 조건을 위해 바로 break 해주기
        print(i)
        break
        
    if i==n: #생성자가 없을 경우에는 0출력하기
        print(0)


# In[5]:


#2292번 벌집
#a += b는 a = a + b와 같다
#6의 배수로 증가하는 중이다

n=int(input())

nums=1 #벌집의 개수 1에서 부터 시작
cnt=1 #횟수

while n>nums: #증가하는 숫자가 입력받은 수인 n에 도달할 때까지만 하고 반복 횟수를 cnt로 카운트해서 cnt를 최종적으로 출력하도록
    nums += 6 * cnt #벌집이 6의 배수로 증가, nums=nums + (6 * cnt)
    cnt += 1 #cnt는 while문이 반복되는 동안 1씩 증가하는 수
print(cnt)


# In[ ]:


#2609번 최대공약수와 최소공배수
#유클리드 호제법
#호제법이란 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘
#a를 b로 나눈 나머지를 r이라 하면 a와 b의 최대공약수는 b와 r의 최대공약수와 같다
#즉, b를 r로 나눈 나머지 r'을 구하고 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 됐을때 나누는 수가 s와b의 최대공약수이다

a,b=map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))


# In[9]:


#2751번 수 정렬하기2
#병합정렬 이해가 안됨


n=int(input())
a=[]
for _ in range(n):
    a.append(int(input())

             
a.sort()
for i in a:
    print(i)
    


# In[2]:


#2775 부녀회장이 될테야
#3층 3호수 사람 수 = 3층 2호수 사람 + 2층 3호수 사람

t=int(input())

for _ in range(t):
    k=int(input()) #층
    n=int(input()) #호 #여기까진 안보고 했음
    f0=[x for x in range(1,n+1)] #0층 리스트 #지능형 리스트 - f0에 다이렉트로 1부터 n+1까지 리스트 형식으로 넣는 다는 뜻이구나
    print(f0)
    for _ in range(k): #층 수만큼 반복
        for i in range(1,n):#1~n-1까지
            f0[i] += f0[i-1] #층별 각 호실의 사람 수를 변경 #f0[i]는 밑에 층 같은 호수 사람 수 #f0[i-1]은 같은 층 전 호수 사람
        print(f0)
    print(f0[-1]) #리스트 중 가장 마지막 수 출력


# 

# In[4]:


#2798번 블랙잭
n,m = map(int,input().split())
a=list(map(int,input().split())
result=0
for i in range(n-2):
       for j in range(i+1,n-1):
           for k in range(j+1,n): #3줄은 변수가 겹치지 않으면서 모든 수를 탐색할 수 있게 해준다. 부르트캠프, 완전탐색
               r=a[i]+a[j]+a[k]
               if r <=m and r> result:
                    result=r
print(result)


# In[ ]:




