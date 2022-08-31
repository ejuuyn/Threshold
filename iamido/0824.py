#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1654 랜선자르기


# In[ ]:


#1874 스택수열


# In[ ]:


#1966 프린터 큐


# In[40]:


#2164 카드2; 1이 맨 위 N이 제일 아래인 n장의 카드 뭉치
#제일 위는 버리고 그다음 제일 위는 제일 아래에 옮김. 
#마지막에 남는 카드 구하기
#4_1234>234>342>42>24>4
#while 써? for면 n+1?
#큐를 써야한다고? queue 는 선입선출. 맨 왼쪽에서 삭제, 맨 오른쪽에 값 넣기
#deque는 양쪽에 값 추가 혹ㄹ은 삭제 가능. 

#출력초과됨. 왜?ㅠ

from collections import deque #라이브러리 사용_덱을 가져와야 함. 
#collections는 파이썬의 표준 라이브러리
q=deque() #덱 생성

N=int(input())
for i in range(N):
    q.appendleft(i+1)#append는 맨 오른쪽. 얘는 맨 왼쪽에 입력. 하나씩 더해서 N까지
    #1>21>321>4321
print(q) #맨처음의 카드 뭉치를 보여줌.

while True:
    if len(q)==1:#한 장이면 할 필요 X. 섞을 카드 없고 걍 1
        print(q[0])
        break
    q.pop() #제일 끝에 요소(인덱스)가 삭제. cf.popleft는 제일 앞이 삭제
    q.rotate(1) #오른쪽으로 이동(제일 뒤가 젤 앞으로). 12345 > 51234
    #1 대신 -1 대입하면 제일 앞에 있던 게 젤 뒤로
    print(q)


# In[4]:


#2231 분해합; N과 N을 이루는 각 자리수의 합. M의 분해합이 N, M은 N의 생성자. 
#ex.245의 분해합 256(245+2+4+5)
#N의 가장 작은 생성자 구하기. 생성자가 없을 경우 0 출력

N=int(input())

for i in range(N+1): #N까지 후보로 침. 
    plus=0
    i=str(i) #문자화 시켜서 자리수별로 쪼개려고
    for j in range(len(i)): #숫자 자리수만큼
        plus +=int(i[j]) #plus에 더해서 값 넣을 거니까 다시 숫자화
    if plus +int(i)==N: #생성자가 없는 경우
        break
        
if N==int(i):
    print("0")
else:
    print(i)



# In[8]:


#2292 벌집; (벌집 모양)중앙 기준으로 1씩 증가하는 숫자. '
#중앙 1에서 N까지 갈 때, 최소 개수의 방(시작, 끝 포함)_6의 배수
#6으로 나눠서 나머지 버리고 +1하면.. dma...
#6(2~7), 12(8~19), 18(20~37)
#"//" 나누기의 몫만 가져옴

N=int(input())
R=1

while N>1:
    N-=(6*R) #한 단계당 6의 n배수만큼 빼기->한 층씩 빼다가 N이 0이나 음수가 되면 그 층이구나
    R+=1
print(R)


# In[12]:


#2609 최대공약수와 최소공배수. 자연수 2개 받아서 출력하기
#첫줄 최대공약수. 둘재 줄 최소공배수
#아래 코딩 틀림. 왜????????????????? 나오잖아;

m,n=map(int,input().split())

for i in range(min(m,n),0,-1): #더 작은 수 기준으로 0까지 하나씩 내려가면서 나눠보기
    if m%i==0 and n%i==0:
        print(i)
        break #최대 약수 나오면 끝내기
    
for j in range(max(m,n),(m*n)):#더 큰 수 기준으로 두 수의 곱까지가 범위
    if j%m==0 and j%n==0:
        print(j)
        break #최소 배수 나오면 끝내기


# In[30]:


#2751 수 정렬하기2
#N개의 숫자. 오름차순으로 정렬

#런타임 에러ㅜ

import sys #파이썬 인터르티터 제어

input=sys.stdin.readline #이거 안 하면 시간 초과라는데
#한두줄 입력 받는 게 아니라 반복문으로 여러줄 입력 받아야 할 때 걍 input 쓰면 시간초과 남. 

N=int(input())
n_list=[] #n개만큼 또 입력받아야 하니까 일단 비워두고

for i in range(N+1):
    n_list.append(int(input())) #리스트에 입력 받은 값들 넣어주고
    
n_list.sort() #오름차순으로 정렬. sort는 기본적으로 리스트를 오름차순 정렬해줌.

for j in n_list:
    print(j)


# In[16]:


#2775 부녀회장이 될테야;아파트 어디냐 거주조건 웨 절애;
#a층 b호에 살면 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람 데려와살아야함
#k층 n호에는 몇 명 사는지 출력
#0층이 시작. 0층 i호에는 i명
#K는 1 이상. N은 14 이하_102호:3명.114호:105명_말이되냐ㅜ
#시그마. 재귀함수. k층 n호에 사는 사람 수 P(k,n)이라고 정의하면
#P(k,n)=P(k-1,1)+P(k-1,2)+...+P(k-1,n)

#시간 초과^!^

for t in range(int(input())):
    def P(k,n): #하나 이름 지어 준 거. 함수 정의 
        if k==0:
            return n
        else:
            sum=0
            for j in range(1,n+1):
                sum+=P(k-1,j) 
            return sum #위의까지의 값을 sum에다 반환 시키는 거. += 사용 보다 크게 활용 가능한가?
        #약간 대명사 느낌으로?-?
        
    k=int(input())
    n=int(input())
    print(P(k,n))


# In[18]:


#2798 블랙잭; 카드의 합이 21 넘지 않는 한도에서 카드의 함 최대
#N장의 카드. 딜러가 외치는 숫자 M(21 대신의 숫자)
#N장의 카드에서 3장 골라서 합 최대로
#첫째줄에 n,m 둘째줄에 카드 숫자들(리스트로 받아야?)
#틀렸대. 왜?

N,M=map(int, input().split())
card=list(map(int, input().split()))
sum_list=[]

for i in range(N):
    for j in range(i+1,N):
        for y in range(i+2,N):
            if card[i]+card[j]+card[y] > M:
                pass #M 초과하면 제외
            else:
                sum_list.append(card[i]+card[j]+card[y])
                #M 초과하지 않으면 합 리스트에 넣고
                
print(max(sum_list))
                


# In[34]:


#2805 나무 자르기; 필요한 나무 미터=M, 절단기에 지정된 높이 = H
#H 그 이상인 부분만, 이하면 안 잘려
#첫째줄은 M,H. 둘째줄은 나무의 높이들 리스트
#이분탐색?

import sys
input=sys.stdin.readline

N,H=map(int,input().split())
h_list=list(map(int,input().split()))

start=0
end=max(h_list)

while start <= end:
    mid=(start+end)//2
    total=0 #잘린 나무의 합
    for i in total:
        if i >mid: #mid보다 크면 잘림
            total +=i-mid
    
    if total >= M: #원하는 높이보다 많이 잘렸으면
        start=mid+1 #자르는 기준점을 높이는
    else: #원하는 높이보다 덜 잘렸으면
        end=mid-1
        
print(end)


# In[38]:


import sys
input=sys.stdin.readline

N,H=map(int,input().split())
h_list=[]
for i in range(N+1):
    h_list.append(int(input()))

start=0
end=max(h_list)

while start <= end:
    mid=(start+end)//2
    total=0 #잘린 나무의 합
    for i in total:
        if i >mid: #mid보다 크면 잘림
            total +=i-mid
    
    if total >= H: #원하는 높이보다 많이 잘렸으면
        start=mid+1 #자르는 기준점을 높이는
    else: #원하는 높이보다 덜 잘렸으면
        end=mid-1
        
print(end)


# In[ ]:


#2839 설탕 배달


# In[36]:


#2869 달팽이는 올라가고 싶다



# In[ ]:





# In[ ]:




