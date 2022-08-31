#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2164

'''
0. 1부터 N까지 등차수열 리스트로 생성
1. 1234 -> 342 -> 24 -> 4
2. 첫 번째 요소 삭제
3. '가운데 - 끝 - 처음' 순으로 바꾸기
4. 하나만 남을 때까지 반복
'''
'''
1. deque: 앞, 뒤에서 데이터를 처리할 수 있는 양방향 자료형(출입구가 양쪽에 있음)으로, 스택처럼 써도 되고 큐처럼 써도 됨
  * 큐(queue): 한쪽 끝으로 자료를 넣고, 반대쪽에서는 자료를 뺄 수 있는 선형구조(FIFO)
2. collections.deque 모듈: deque 자료형을 생성하는 모듈
3.  deque 메소드 설명: https://velog.io/@nayoon-kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-deque
'''
'''
1. popleft() - 맨 왼쪽 요소를 삭제하고 반환
2. rotate(n) - n만큼 오른쪽으로 회전. n이 음수면 왼쪽으로 회전
--> 1만큼 왼쪽으로 회전해야 할 듯
'''

from collections import deque
N = int(input())
queue = deque()

while True:
    if len(queue) == 1:
        print(queue)
        break
    if len(queue) > 1:
        queue.popleft()
        queue.rotate(1)
        print(queue)
        
'''
모르겠당ㅎ
'''


# In[1]:


from collections import deque
n = int(input())  # n 입력
queue = deque()  # queue 변수를 deque 형태로 선언

for i in range(1, n+1):  
    queue.append(i)  # queue에 1부터 n까지 삽입
    
while len(queue) > 1:
    queue.popleft()  # 맨 왼쪽 요소 제거
    queue.rotate(-1)  # 왼쪽으로 1만큼 회전
    
print(queue[0])  # print(queue)로 하면 deque([2])로 출력되던데 왜 그러는 건지 모르겠음


# In[9]:


# 2231

'''
자연수 n의 분해합: n과 n을 이루는 각 자리수의 합
자연수 m의 분해합이 n인 경우, m은 n의 생성자 
'''
'''
1. 자연수 n 입력
2. n을 문자열로 바꿔서 각 자리수의 합 구하기 + n
3. 모르겠음..문제 이해가 안 됨..
'''

n = int(input())

for i in range(n):
    m = sum(map(int, str(i)))  # 자리수 합 구하기
    n_sum = i + m  # 분해합 구하기
    if n_sum == n:
        print(i)
        break
else:
    print(0)
    


# In[ ]:


# 2292

'''
0. 벌집 만들기: 왼쪽으로 1씩 증가하면서 회전
1. 한 겹의 칸 개수는 6의 배수씩 증가 (1, 6, 12, 18, ...) -> 각 겹의 마지막 칸 숫자 구하는 수열 공식 세움
'''

n = int(input())

m = 1  # 한 겹 당 칸 개수
cnt = 1  # 1에서 n까지 갈 때 지나가는 방의 최소값

while n > m:
    m += 6 * cnt
    cnt += 1
print(cnt)


# In[ ]:


'''
0. 구간을 나눠서 n이 어디 구간에 속하는지 구하면 되지 않을까
1. 1개 지날 때: 1 / 2개: 2~7 / 3개: 8~19 / 4개: 20~37 / 5개: 38~61
2. 수열: a1 = 1, an = 6(n-1) -> 리스트 만들어야 하나..?
3. 모르겠다
'''

N = int(input())  # N 입력

a1 = 1  # 첫 항 지정

while n > a1:  # 수열 공식 지정
    an = 6 * (n-1)
    n += 1    
    


# In[1]:


# 2609_최대공약수와 최소공배수

'''
0. 유클리드 호제법: 2개의 자연수의 최대공약수를 구하는 알고리즘

'''

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


# In[2]:


'''
math 모듈에 최대공약수, 최소공배수 구하는 함수 있음
'''

import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))


# In[ ]:


##### 2751_수 정렬하기2

'''
0. 수의 개수 N 입력 -> 빈 리스트 만들어서 수 입력
1. list.sort() 함수로 정렬
'''

n = int(input())  # 수의 개수
num = []  # 수 입력할 빈 리스트

for i in range(n):
    num.append(int(input()))  # n개의 수를 리스트에 입력

num.sort()  # 리스트를 오름차순으로 정렬(sort는 오름차순이 기본)

for i in num:
    print(i)  # 리스트 안의 요소를 차례대로 출력
    
'''
시간초과..
'''


# In[ ]:


'''
0. n의 범위가 1부터 1,000,000까지 -> input()으로 최대값까지 입력 받으면 시간이 오래 걸림 (특히 반복문 안에서는 더 오래 걸린다고 함)
1. 해결방법: import sys / sys.stdin.readline()
# input 과 sys.stdin.readline의 차이점: https://buyandpray.tistory.com/7
'''

import sys

n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
    
num.sort()

for i in num:
    print(i)


# In[ ]:


# 2775_부녀회장이 될테야

'''
0. a층의 b호에 살려면 아래층(a-1)의 1호부터 b호까지 사람들 수의 합만큼 데려와 살아야 함
   -> k층 n호에 살고 있는 사람 수 구하기
'''

t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
    print(f0[-1])

