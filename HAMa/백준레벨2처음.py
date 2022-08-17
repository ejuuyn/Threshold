#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#백준 1018 체스판 다시그리기
n, m = map(int,input().split())  #정수 받기: 원래 판의 배열
first_board =[]                  #원래 판을 리스트로 
edited_board = []                #수정된 판을 리스트로

for _ in range(n):
    first_board.append(input())   #n(행)의 개수만큼 원래의 판을 입력(리스트로)
    
for a in range(n-7):         #전체 체스판에서 시작점을 잡기위함.
    for b in range(m-7):     #(-7)을 통해 8*8판의 시작점의 위치를 확인   
        index1 = 0           #index1 <- W로 시작할 경우 바뀐 체스판    
        index2 = 0           #index2 <- B로 시작할 경우의 체스판
        for i in range(a, a+8):
            for j in range(b,b+8):   #a,b모두 열의 시작점을 기준으로 +8
                if (i+j)%2 == 0:     #행+열이 짝수 -> 시작점의 색과 같은 색
                    if first_board[i][j] != 'W':  #W가 아닐때 #!= 같지않다.
                        index1 += 1   #왜 index1을 'W'로 시작하는 체스판으로 설정해놓고 'W'가 아닐때 1을 더해줄까?
                    if first_board[i][j] != 'B':
                        index2 += 1
                else:                #행번호+열번호 != 짞수
                    if first_board[i][j] != 'B':
                        index1 += 1
                    if first_board[i][j] != 'W':
                        index2 += 1
        edited_board.append(min(index1,index2))  #바뀐 체스판의 수 중 작은수를 edited_board 리스트에 추가

print(min(edited_board))


# In[ ]:


#백준 1085 직사각형 탈출
x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))         #경계면 까지 가장 가까운 거리 구하기.


# In[ ]:


#백준 1181 단어정렬  
#sort는 문자열도 정렬해준다. 권정열아님.
#input()은 겁나 느리다. 아하.!

n = int(input())
list1=[]

for i in range(n):
    list1.append(input()) #솔직히 append 뭔지 아직 1도 모르겠음 ㅋㅋ
    
set_list1=set(list1) ##set으로 변환해서 중복값을 제거 ## set이 뭔데..?
list1= list(set_list1)

list1.sort()   ## 괄호안에 아무 값도 넣지 않으면 알파벳 순서대로 ㄷ정렬을 해준다.!!
list1.sort(key = len) ##sort key는 len 순서대로!.

for i in list1:
    print(i)


# In[ ]:


#백준 1259 펠린드롬수

while True:          #while True 왜?
    n = input()
    
    if n == '0':    #0 못오기로 약속~
        break
        
    if n==n[::-1]:   #[::-1]로 반전
        print('yes')
    else:
        print('no')
        


# In[1]:


#백준 1436 영화감독 숌

n = int(input())
count = 0
six_n =666
 
while True :
    if '666' in str(six_n):
        count += 1
    if count == n:
        print(six_n)
        break
    six_n += 1

# 사실 뭔지 모르겠습니다. ..
    


# In[ ]:


#백준 1654 랜선 자르기
#솔직히 반에 반에 반도 이해가 안됨..모르는 함수도 많고.. 시간 내서 공부 더 할게.
import sys #이게 뭐죠?

L , N = map(int,input().split())  #랜선의 길이를 담은 리스트
lan= [int(input()) for i in range(L)]  #갖고 있는 랜선 중 최대값
max_lan = max(lan) #후보군을 담을 리스트
res =[]

def binary(k,start, end):   #이분 탐색 시작
    
    while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
        mid = (start+end)//2 #중간 위치
        lines = 0 #랜선 수
        for i in lan :    #구해진 값으로 랜선을 잘라보기 
            lines += i // mid # 분할된 랜선 수 
        #자른 랜선들이 N보다 작으면 조금 더 작게 잘라야 함
        
        if lines < N: #랜선의 개수가 분기점
            end = mid -1   #조건을 만족하는 경우
        else:              #후보군에 넣고 좀 더 크게 만들어보기
            res.append(mid)
            start = mid +1
        
binary(N,1,max_lan)  #이분탐색 함수 호출

print(max(res))  #후보군에서 최대값 출력


# In[2]:


##### 백준 1874 스택수열 #이건 문제 자체가 이해가 안됨..
#일단 작성만 합니다. 배껴서

n = int(input())
s=[]
op=[]
count =1 
temp =True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
        


# In[4]:


#백준 1920 수찾기 (1).이분탐색
# 문제 설명 
# N개의 정수가 들어있는 집합 A
# M개의 정수가 들어있는 집합 B
# 집합 B의 요소들이 집합 A에 포함되어있는지 확인하기

from  sys import stdin,stdout
n=stdin.readline()
N=sorted(map(int,stdin.readline().split()))
m=stdin.readline()
M=map(int,stdin.readline().split())

def binary(l,N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l<N[m]:
        return binary(l,N,start,m-1)
    else:
        return binary(l,N,m+1,end)
    
for l in M:
    start = 0
    end = len(N)-1
    print (binary(l,N,start,end))
    


# In[6]:


#백준 1920 수찾기 (2).집합자료형을 통한 포함여부 확인
# 문제 설명 
# N개의 정수가 들어있는 집합 A
# M개의 정수가 들어있는 집합 B
# 집합 B의 요소들이 집합 A에 포함되어있는지 확인하기

from sys import stdin, stdout
n= stdin.readline()
N= set(stdin.readline().split())
m=stdin.readline()
M= stdin.readline().split()

for l in M :
    stdout.write('1\n') if l in N else stdout.write('0\n')
    


# In[ ]:


#백준 1929 소수 구하기 
M,N = map(int,input().split())


for i in range(M,N+1):
    if i == 1:   #1은 소수가 아니기 때에
        continue
    for j in range(2, int(i** 0.5)+1 ): 
        if i%j == 0:
            break
    else:
        print(i)
    


# In[ ]:




