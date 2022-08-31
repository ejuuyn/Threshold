#!/usr/bin/env python
# coding: utf-8

# # 1018번 체스판 다시 칠하기

# In[47]:


'''
흰/검 교차
교체해야하는 최소 보드 개수?
변을 공유하는 '두'개의 사각형은 서로다른 색

문제:
1.어떻게 M*N에서 교체소요가 가장 작은 8*8블럭을 찾아 내는가
-(모든 지점에서 교체소요를 구하고 최소값을 구해볼까)
2.어떤 방식으로 교체를 할 것인가
-(오른쪽과 아래만 다른 색이면 모두 성립) 

백준은 왜 넘파이를 지원하지 않는가

for i in list:
if i==i+1:
  if i=='B':
       list[i]='W'
  else:
       list[i]='B'
대충 이런느낌?  
'''
M,N=map(int,input().split())
num_list=[]
board_list=[]
for i in range(M):
    board_list.append(input().upper())
for i in range(M-7):
    for j in range(N-7):
        num_b=0
        num_w=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2!=0:
                    if board_list[x][y]=='B':
                        num_b+=1
                    else:
                        num_w+=1
                else:
                    if board_list[x][y]=='W':
                        num_w+=1
                    else:
                        num_b+=1
                num_list.append(min(num_w,num_b))
print(min(num_list))


# # 1085번 직사각형에서 탈출

# In[52]:


'''
한수 (x,y) 직사각형 각 변 좌표축에 평행, 왼쪽 아래 꼭지점이 (0,0)
직사각형의 경계선 까지 거리의 최소값 직사각형(0,0)-(w,h)
1. 한 점에서 직선까지의 거리 d=|ax+by+c|/root(a^2+b^2)
2. (x,y)에서 y=0, x=0, y=w, y=h 까지의 거리를 모두 구한 후 최솟값 구하는 알고리즘
'''
x,y,w,h=map(int,input().split())
d=[]
d.append(abs(x-w))
d.append(x)
d.append(abs(y-h))
d.append(y)
print(min(d))


# # 1181번 단어 정렬

# In[57]:


'''
1.길이가 짧은 것 부터
2.길이가 같으면 사전 순으로
단어를 정렬하는 알고리즘
생각
1.sort함수로 간단하게 해볼까
2.길이 같은거 안되면 if문이나 try문 하면 될듯
'''
N=int(input())
word=set()
for i in range(N):
    word.add(input())
word=list(word)
word.sort()
word.sort(key=len)
print("\n".join(word))


# # 1259 펠린드롬수

# In[ ]:


'''
앞으로 읽어도 뒤로 읽어도 우영우
기러기 토마토 스위스 인도인 별똥별 우영우 역삼역?
=펠린드롬
펠린드롬수 나오면 yes 아니면 no
생각
1.리스트로 만들어서 [::-1]과 동일하면 yes
2.입력을 여러개 받아야 하므로 while문 쓰자
'''
while 1:
    p=input()
    if p=='0':
        break
    if p==p[::-1]:
        print('yes')
    else:
        print('no')


# # 1436번 영화감독 숌

# In[27]:


'''
666 1666 2666 3666 4666 5666 6661 6666 ...
N번째 종말의 숫자 구하기
생각
1.종말의 숫자 리스트 정렬-(666을 하나의 묶음으로 보고 어떻게 해봅시다) in method
2.N인덱스로 뽑아오기 가능?
'''
N=int(input())
ter=[]
for i in range(N**10):
    if '666' in str(i):
        ter.append(str(i))
    if len(ter)==N:
        break
if N==1:
    print("666")
elif N==2:
    print("1666")
else:
    print(ter[-1])


# In[4]:


ter=[]
for i in range(N**2):
    if '666' in str(i):
        ter.append(str(i))
ter


# # 1654번 랜선 자르기

# In[31]:


'''
N개의 랜선 필요
K개의 랜선 보유 but 길이 제각각
K개의 랜선을 잘라서 N개 만들기
생각
길이로 접근을 해야겠다
---
생각 자체는 맞았으나 문제에서 요구한 수가 큰 관계로 시간초과 발생->이분탐색 해야한다고 함
1.K개의 랜선의 길이를 다 더한 값을 N개로 나눠서
2.K(i)번째 수를 1에서 나온 값으로 나눠진 몫의 합이 N이 되는 지점 찾으면 되지 않을까요
'''
k,n=map(int,input().split())
k_list=[]
for i in range(k):
    k_list.append(int(input()))
avg=sum(k_list)//n
for i in range(avg,0,-1):
    sumki=[]
    for j in k_list:
        sumki.append(j//i)
    if sum(sumki)==n:
        print(i)
        break    


# # 1874번 스택 수열

# In[11]:


'''
스택 LIFO 123456789->987654321
스택으로 수열 만들기 스택에 푸쉬하는 수는 오름차순 
리스트 두개 만들어서 옮겨넣는 식으로 진행해보자
생각
1.수열을 받은 후 그 수열을 만드는 것이 가능한지 아닌지를 어떻게 알아볼 수 있을까
-(1번 리스트에서 2번 리스트로 옮길 순서가 맞지 않으면
--pop으로 제거하면서 옮기는데 순서가 맞지 않으면 이미 제거되서 오류나올 듯
--- + -없이 바로 no가 나와야 하니까 선 계산 후 출력
2.머리속으로 정리가 잘 안되는데 일단 하면서 생각해보자
차집합 실패-반복하는 과정에서 순서 뒤죽박죽 됨
이거 스택으로도 가능할 듯 
'''
n=int(input())
arr1=[]
arr2=[]
arr3=[]
pm=['+']
for i in range(n):
    arr1.append(int(input()))
arr1_copy=arr1.copy()
for i in range(1,n+1):
    arr2.append(i)
    try:
        while 1:
            if arr2[-1]==arr1[0]:
                arr3.append(arr2.pop())
                del arr1[0]
                pm.append('-')
            else:
                pm.append('+')
                break
    except:
        continue
if arr3==arr1_copy:
    print("\n".join(pm))
else:
    print('NO')
'''
문제점
1. if절에서 리스트에 추가되는 동시에 빠져나가 + - 순서가 이상해짐
2. while 문 반복을 하다보니 +가 이상하게 붙는 현상 발생


# In[ ]:


n=int(input())
arr1=[]
arr2=[]
arr3=[]
pm=[]
for i in range(n):
    arr1.append(int(input()))
arr1_copy=arr1.copy()
for i in range(1,n+1):
    arr2.append(i)
    for j in i:
        if arr2[-1]==arr1[0]:
            arr3.append(arr2.pop())
            del arr1[0]
            pm.append('-')
        


# # 1920번 수 찾기

# In[17]:


'''
n개의 정수 안에 x라는 정수가 있는지
있으면 1 없으면 0
정수 범위가 시간초과 걸리기 딱 좋아 보이는듯
생각
1.일반적으로 하면 시간초과 걸릴게 뻔한데 어떻게 줄이지
2.리스트로 만들어서 in 함수 쓰기
역시나 시간초과...
--
리스트 말고 집합으로 푸니 되긴 함
리스트는 탐색에서 O(N)의 시간복잡도를 쓰지만 집합은 O(1)의 시간복잡도를 쓰기 때문
자료형에 따른 시간복잡도(https://chancoding.tistory.com/43)
이분탐색 방법으로도 풀 수 있음
'''
n=int(input())
n_list=set(map(int,input().split()))
m=int(input())
m_list=map(int,input().split())

for i in m_list:
    if i in n_list:
        print('1')
    else:
        print('0')


# # 1929번 소수 구하기

# In[50]:


'''
m이상 n이하의 소수 출력
N이 100만까지
생각
1.N-M까지 수를 리스트에 넣고
2.리스트 원소가 소수인지 판별만 하면
3.소수판정방법은? 1과 자기 자신만을 약수로 가지는 수 
4.시간복잡도 신경써야할라나
찾아내고 싶은 범위만큼 자연수를 죽 늘어놓는다.
1은 수학적으로 소수도, 합성수도 아닌 유일한 자연수이므로 먼저 1을 지운다.
먼저 2를 소수로 표시하고 2를 제외한 2의 배수(4, 6, 8, ...)를 모두[21] 소거한다.
그 다음 3을 소수로 표시하고 남아있는 수 중 3을 제외한 3의 배수(9, 15, 21, ...)도 모두[22] 소거한다.
그 다음 5를 소수로 표시하고 남아있는 수 중 5를 제외한 5의 배수(25, 35, 55, ...)도 모두[23] 소거한다.
그 다음 7을 소수로 표시하고 남아있는 수 중 7을 제외한 7의 배수(49, 77, 91, ...)도 모두[24] 소거한다.
남아있는 가장 작은 수(소수)에 대해 이 과정을 \sqrt n 
n
​
  보다 작거나 같은 소수까지 계속 반복한다.
--
이거..왜 틀린거야..?
'''

m,n=map(int,input().split())
mn=set()
for i in range(m,n+1):
    mn.add(i)
if 1 in mn:
    mn.discard(1)
for i in range(2,int(n**(1/2))+1):
    for j in range(i,(n//i)+1):
        mn.discard(i*j)
mn_list=list(map(str,mn))
print("\n".join(mn_list))


# # 1966 프린터 큐

# In[59]:


'''
프린터 큐의 FIFO
큐의 중요도 확인 후 뒤에 문서들 중 중요도가 하나라도 높은게 있으면 제일 뒤로 보냄
->중요도가 제일 높은 순으로 프린터 진행
테스트케이스 t개 문서의 개수 n개 궁금한 문서가 현재 Queue에서 M번째(왼쪽부터 0)
다음줄 중요도 n개
생각
1.중요도와 문서 순서를 딕셔너리로 연결하자
2.중요도(value값)으로 정렬하고 뽑으면 되지 않을까?
'''
T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    n1=[] #key
    for j in range(n):
        n1.append(j)
    imp=list(map(int,input().split())) #value
    dic=dict(zip(n1,imp))
    for j in range(n):
        for k in range(n):
            if dic.value(0)<dic.value(j):
                move_to_end(dic.value(0))
print(dic)


# In[ ]:


T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    n1=[]
    for j in range(n):
        n1.append(j)
    imp=list(map(int,input().split())) 


# # 1978번 소수 찾기

# In[53]:


'''
위에 소수 찾은 방법으로 끌어오면 되지 않을까
'''
sosu=set()
for i in range(2,1000):
    sosu.add(i)
for i in range(2,32):
    for j in range(i,(1000//i)+1):
        sosu.discard(i*j)
N=int(input())
nn=list(map(int,input().split()))
num=0
for i in range(N):
    if nn[i] in sosu:
        num+=1
print(num)
    


# In[73]:


'''
N개의 수에서 산술평균,중앙값,최빈값,범위 구하기
N은 홀수
생각
1.산술평균 다 더해서 N으로 나눈 몫
2.중앙값 원소 n개의 리스트 정렬시키고 나서 l[n//2]
3.최빈값 max(count(i))
4.범위 max()-min()
'''

n=int(input())
integer=[]
for i in range(n):
    integer.append(int(input()))
#1 산술평균
print(round(sum(integer)/n))
#2 중앙값
print(sorted(integer)[n//2])
#3 최빈값
ssn=list(set(integer))
int_count={}
for i in ssn:
    int_count[i]=integer.count(i)
max_count=max(int_count.value())
print(integer[int_count[max(int_count)]])

#4 범위
print(max(integer)-min(integer))


# In[ ]:




