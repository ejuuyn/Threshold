#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1552번 단어 수 세기

t=input().split() #split()은 띄어쓰기가 된 글자마다 글자를 잘라줌
print(len(t)) #len은 ()안의 글자 세주는 함수


# In[ ]:


#1157번 많이 사용된 대문자 출력하기
t=input().upper() #처음에 입력받는 문자는 대소문자를 구분하지 않기 때문에 upper함수를 통해 문자열을 모두 대문자로 변환
                    #넣은 값 중에서 가장 많이 나온 알파벳을 '대문자'로 출력하기 때문에 입력값 전부 대문자로 바꿔준다
at=list(set(t)) #set함수를 통해 중복되는 값 제거하고 나머지 요소들은 at 변수에 저장

cnt_list=[]
for x in at:
    cnt=t.count(x) #입력받은 문자열에 같은 알파벳이 몇 개 있는지 숫자 카운트해서 cnt_list에 추가한다
    cnt_list.append(cnt) #count 숫자를 리스트에 append(덧붙인다) 한다

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_inedx=cnt_list.index(max(cnt_list))
    print(at[max_index])
#index함수 모름
# for in 구문 모름
# max함수가 갑자기 왜 나오지?


# In[11]:


#1546번 평균 구하기
n=int(input()) #과목수
test_list=list(map(int, input().split())) #시험 점수는 list자료형으로 선언
max_score=max(test_list) #새로운 점수를 구하기 위해서는 입력받은 점수 중 가장 큰 점수를 찾아야하기 때문에 
               
new_list=[] #빈 리스트 생성
for score in test_list: #for문을 이용해서 입력받은 시험 점수를 하나씩 꺼냄
    new_list.append(score/max_score *100) #그리고 리스트에 계산해서 새로운 점수를 리스트에 추가한다
test_avg=sum(new_list)/n #그리고 평균을 구한다
               
print(test_avg)


# In[14]:


#2439번 숫자를 별로 출력하기
n=int(input()) #이제 숫자 입력은 가능하다

for i in range(1, n+1): #range(초기값,마지막값,증가값)란 뜻입니다
    print(" "*(n-i)+"*"*i) #공백을 n-i만큼 곱하고 *을 i만큼 넣고 합치기


# In[15]:


#2562번 9개의 값 중 최댓값 구하기
n=[] #빈 리스트 생성
for _ in range(9): #문제 자체가 9개 중 하나임
    i=int(input())
    n.append(i) #입력값을 append함수로 요소 추가

print(max(n))
print(n.index(max(n))+1) #index는 함수 위치 찾기 인덱스는 0부터 시작이니 +1 해야함


# In[ ]:


#2577번 0부터 9까지 몇 번 쓰였을까?
a=int(input())
b=int(input())
c=int(input())
result=list(str(a*b*c)) #곱한 값을 문자열(str)로 변환하고 list로 묶는다

for i in range(10): #i=0~9까지라는 뜻
    print(result.count(str(i))) # i를 문자열(str)로 바꿔서 몇 개 있는지 세기(count는 str만 사용 가능)


# In[ ]:


#2675번 문자열 반복
n=int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt),end='')
    print()


# In[ ]:


#2742번 하나씩 찍기
n=int(input())

for i in range(n,0,-1):
    print(i)

