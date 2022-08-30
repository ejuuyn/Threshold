#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2839_설탕 배달

'''
0. 3kg, 5kg 봉지로 Nkg 설탕 배달 -> 봉지의 최소 개수
1. 5kg 봉지로 먼저 나눠 담고 남는건 3kg?
2. n이 5로 나누어 떨어질 때: n / 5 = m -> min(k) = m (k=5kg 봉지 개수)
3. n이 5로 나누어 떨어지지 않을 때: n / 5 = m...r -> min(k) = m + i (i = 3kg 봉지 개수, 1 or 2)
3-1. r<4: i = 1
3-2. r=4: i = 2
'''

n = int(input())
k = 0  # 5kg 봉지 개수
i = 0  # 3kg 봉지 개수
cnt = 0  # 총 봉지 개수

while 


# In[3]:


sugar = int(input())  # 설탕 무게 입력

bag = 0  # 봉지 개수 

while sugar >= 0:
    if sugar % 5 == 0:  # 5의 배수일 때
        bag += (sugar//5)  # 5로 나눈 몫이 봉지 개수
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
    print(-1)


# In[6]:


#2869_달팽이는 올라가고 싶다

'''
0. 나무 높이 = v, 낮에 오르는 높이 = a, 밤에 미끄러지는 높이 = b -> 정상까지 며칠?
1. if) v=10, a=5, b=2 -> 하루 3m 오름 -> 4일 소요 => 소수점 올림 해야겠네
2. 하루에 오르는 높이 = a-b
3. n번 오르고 n-1번 미끄러짐 -> v = an - b(n-1) -> n = (v-b)/(a-b)
4. (v-b)/(a-b)의 나머지가 0이 아니면 +1
'''

a, b, v= map(int, input().split())

if (v-b)%(a-b) == 0:  # %: 나누기의 몫이 아닌 나머지를 구함
    print((v-b)//(a-b))
else:
    print(((v-b)//(a-b))+1)


# In[2]:


#4153_직각삼각형

'''
0. 피타고라스 정리: 밑변^2+높이^2=빗변^2
1. 빗변이 가장 길어야 함
2. 정수 3개 중 max가 빗변, 나머지 값들의 제곱합=빗변제곱
'''
'''
remove(): array 내 요소 삭제
- array.remove(x) 형태로 사용 (array 안에 삭제하려는 값이 여러 개가 있더라도 첫 번째 값만 삭제함)
- 모든 값을 삭제하려면 for문을 이용해도 됨
https://ooyoung.tistory.com/49
'''

while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break   # 세 정수의 합이 0이면 종료
    max_num = max(nums)   # 가장 큰 수를 빗변으로 지정
    nums.remove(max_num)   #  빗변을 제외한 나머지 변만 남김
    if nums[0]**2 + nums[1]**2 == max_num**2:   # 피타고라스
        print('right')
    else:
        print('wrong')


# In[1]:


#4949_균형잡힌 세상

'''
<문제>
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
'''
'''
도저히 모르겠어서 베낌
<풀이> - 스택 이용 https://velog.io/@pmk4236/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-Python
1. 점"."이 들어오면 입력 종료
2. 스택 리스트를 만들어서 먼저 발생된 시작되는 괄호 저장, 짝이 맞는 괄호가 생기면 .pop으로 리스트 비움
3. 짝이 맞지 않는 괄호가 생기면 스택 리스트를 그대로 둠
4. 스택의 리스트가 비어있으면 yes, 비어있지 않으면 no 출력

# 스택이란?
스택(stack)은 제한적으로 접근할 수 있는 나열 구조이다. 그 접근 방법은 언제나 목록의 끝에서만 일어난다.
스택은 한 쪽 끝에서만 자료를 넣거나 뺼 수 있는 선형 구조(LIFO)로 되어 있다.
자료를 넣는 것을 push, 꺼내는 것을 pop이라고 한다.
'''

while True:
    a = input()
    stack = []
    
    if a == ".":
        break
        
    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()   # 맞으면 지워서 stack을 비워줌. 0 = yes
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


# In[3]:


#7568_덩치

'''
아니....이게.......

'''

import sys

n = int(sys.stdin.readline())

people = []

for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    people.append([w, h])
    
count_list = []

for j in people:
    count = 1
    for k in range(len(people)):
        if j[0] < people[k][0] and j[1] < people[k][1]:
            count += 1
            
    count_list.append(count)
    
print(' '.join([str(x) for x in count_list]))


# In[ ]:


#9012_괄호

T = int(input())   # 테스트케이스 개수

for i in range(T):   
    stack = []
    a = input()   
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")


# In[4]:


#10250_호텔

'''
<생각 1>
1. 열 먼저 오름차순으로 배정 (101, 201, ..., H01, 102, 202, ..., H02, ..., H0W)
2. 층이 H까지 채워지면 W가 1씩 증가
3. 각 방마다 순서를 지정해놔야 하나? 아닌듯
-> 이거 못해..
'''
'''
<생각 2>
1. 꼭대기층 배정받은 손님 순서(N) = 건물 층수(H)의 배수 -> N/H의 나머지가 0이면 N번째 손님은 꼭대기층 배정
2. 배정 층수 = N/H의 나머지
3. 호수 = N/H의 몫+1
'''

n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())
    x = n % h
    y = n // h +1
    if x == 0:   # 꼭대기층일 떄
        x = h
        y -= 1
    print(x*100+y)


# In[5]:


#10814_나이순 정렬

'''
stable 정렬: 입력 받은 값들 중 같은 값이 있으면 해당 값의 순서를 그대로 유지
lambda: 함수를 생성할 때 사용하는 예약어로, 보통 함수를 한 줄로 간결하게 만들 때 사용
 - lambda 인수1, 인수2, ... : 인수를 이용한 표현식
'''

n = int(input())
member = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member.append((age, name))
    
member.sort(key = lambda x : x[0])   # (age, name)에서 age만 비교

for i in member:
    print(i[0], i[1])


# In[6]:


#10773_제로

'''
몰라 모르겠어 포기...
'''


# In[7]:


#10816_숫자 카드2

'''
모르겠어서 베낌 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10816-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%EC%8B%A4%EB%B2%844-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89
'''

import sys
input = sys.stdin.readline

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
        
def binarySearch(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in candidate:
    print(binarySearch(cards, target, 0, len(cards)-1), end=" ")

