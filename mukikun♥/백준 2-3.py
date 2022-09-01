#!/usr/bin/env python
# coding: utf-8

# # 2839 설탕배달

# In[1]:


'''
3키로 5키로
비커 채우기
3키로 5키로 설탕봉지
최소값
먼저 5키로로 N을 나누고 나머지가 0 혹은 3의 배수이면 출력
아니면 -1 출력하면 될듯
3으로 나누고 나머지가 5의 배수인 경우를 어떻게 표현해야하지
1.5의 배수인 경우
2.5를 계속 빼고 나머지가 3의 배수인 경우
3.cnt를 세서 최소값을 구하는게 더 나을 듯 위에 경우의수는 너무 많은거 같다
'''
N=int(input())
K=N
m=N%5
for i in range(N//5):
    if K%5==0:
        break
    else:
if m==0:
    print(N//5)
elif for i in range(:
    print(N//5+m//3)
else:
    print(-1)


# In[13]:


N=int(input())
K=N
cnt_list=[]
cnt3=0
cnt5=0
if K%5==0:
    for i in range(N//5):
        cnt5+=1
    cnt_list.append(cnt5)
else:
    for j in range(N//5+1):
        cnt3=0
        J=K
        if K%3==0:
            while J!=0:
                J-=3
                cnt3+=1
            cnt_list.append(cnt3+cnt5)
        K-=5
        cnt5+=1
try:
    print(min(cnt_list))
except:
    print(-1)


# # 2869번 달팽이는 올라가고 싶다

# In[ ]:


'''
시간제한 .15초
V미터인 나무막대 낮에 A미터 올라가고 밤에 B미터 미끄러진다
올라간 높이=H 라 하고 if H==V이면 break, 그 전까지 day+=1
시간초과 걸릴려나 일단 해봐 
---
반복문을 쓰면 바로 시간초과 걸릴 듯
정상에 못 올라갔을 때의 H=(a-b)*d
a-b (v-a)//(a-b)만큼 올라가면 다음날 도착
1.v-a를 a-b로 나눈 나머지=0 (v-a)//(a-b)+1
2."    "  >0 v-a//a-b+2
'''
a,b,v=map(int,input().split())
h=0
day=0
while h<=v:
    day+=1
    h+=a
    if h>=v:
        print(day)
        break
    else:
        h-=b


# In[3]:


a,b,v=map(int,input().split())
if (v-a)%(a-b)==0:
    print((v-a)//(a-b)+1)
else:
    print((v-a)//(a-b)+2)


# # 4135번 직각삼각형

# In[1]:


'''
피타고라스의 정리
직각삼각형 TF 여부
'''
while True:
    a,b,c=map(int,input().split())
    if a!=0 or b!=0 or c!=0:
        if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print('right')
        else:
            print('wrong')
    else:
        break


# # 4949번 균형잡힌 세상

# In[5]:


'''
()와 []가 잘 매치되어 있는지 확인
아닌경우를 생각해보자
1.오른쪽 괄호가 없는경우
2.오른쪽 괄호가 먼저 나온경우=(왼쪽 괄호가 없는경우)
아니 어캐해야할지 감도 안잡히는데
왼쪽괄호가 나오면 리스트에 추가하고 오른쪽 괄호가 넣으면 리스트[-1]과 매치시켜서
짝이 맞으면 pop, 안맞으면 break
indexerror 이슈 리스트에 아무것도 추가 안 되어 있는데 오른쪽 괄호를 먼저 받으면
[-1]인덱싱 불가<-리스트가 비어있는 조건 추가로 해결
'''
while True:
    s=input()
    if s==".":
        break
    string=[]
    for i in s:
        if i=='(' or i=='[':
            string.append(i)
        elif i==')':
            if not string:
                string.append(i)
                break
            elif string[-1]=='(':
                string.pop()
            else:
                break
        elif i==']':
            if not string:
                string.append(i)
                break
            elif string[-1]=='[':
                string.pop()
            else:
                break
    if not string:
        print('yes')
    else:
        print('no')


# # 7568번 덩치

# In[21]:


'''
키 몸무게 받고 덩치가 큰 순서대로 
썅 개어렵네 진짜
개빡치ㄴ닥
빡대가린가 왜이렇게 머리가 안돌아가지
no'''
N=int(input())
li=[]
li2=[]
li3=[]
for i in range(N):
    x,y=map(int,input().split())
    li.append((x,y))
for i in li:
    cnt_s=0
    cnt_e=0
    for j in li:   
        if (i[0]>=j[0] and i[1]>j[1]) or (i[0]>j[0] and i[1]>=j[1]):
            continue
        elif (i[0]>j[0] and i[1]<j[1]) or (i[0]<j[0] and i[1]>j[1]) or (i[0]==j[0] and i[1]==j[1]):
            cnt_e+=1
        else:
            cnt_s+=1
    print(cnt_e,cnt_s)    
    li2.append((cnt_e,cnt_s))
for i in range(N):
    cnt=0
    for j in range(N):
        if li2[i]==li2[j]:
            cnt+=1
    li2[i]=li2[i][0]+li2[i][1]-cnt+1
print("".join(str(li2)))


# # 9012번 괄호

# In[38]:


'''
어 이거 위에 균형잡힌 세상이랑 같은문제네
'''
li=[]
li2=[]
t=int(input())
for i in range(t):
    li.append(input())
for i in li:
    for j in i:    
        try:
            if j=='(':
                li2.append(j)
            elif j==')':
                li2.pop()
        except:
            li2.append(j)
            break
    if not li2:
        print('YES')
    else:
        print("NO")
    li2=[]


# # 10250번 ACM호텔

# In[41]:


'''
정문에서 가장 짧은거리 순으로 선착순
각층 1호부터 나가고 2호 3호 순으로
%n써서 YYXX표현하자
H명까지 1호 H+1~2H명까지 2호...사실 w는 큰 의미 없음
yy01호 n명째 X*h~X+1*h-1사이 ->(n-1을 h로 나눈 몫+1)호 5층 5명째->501호 6명째 102호 
(n-1을 h로 나눈 나머지+1)층
'''
t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    if 1<=(n-1)//h+1<=9:
        print("%s0%s"%((n-1)%h+1,(n-1)//h+1))
    else:
        print("%s%s"%((n-1)%h+1,(n-1)//h+1))
        


# # 10773번 제로

# In[42]:


'''
회식 장부 관리 잘못된 수를 부를때매다 0을 외쳐 최근에 쓴 수를 지움_pop()
리스트 만들어서 추가 제거 썸
이게 왜 실버? 이왜실
'''
k=int(input())
li=[]
for i in range(k):
    n=int(input())
    if n==0:
        try:
            li.pop()
        except:
            li.append(0)
    else:
        li.append(n)
print(sum(li))


# # 10814번 나이순 정렬

# In[48]:


'''
회원가입 나이 이름 변수 나눠서 반복문으로 받고
매번 sort때리면 되지 않을까
..시간초과?
'''
n=int(input())
li=[]
for i in range(n):
    age,name=input().split()
    age=int(age)
    li.append((age,name))
li.sort(key=lambda x:x[0])
for x,y in li:
    print(x,y)


# #  10816번 숫자 카드 2

# In[ ]:


'''
1.N개
2.카드에 적혀있는 숫자
3.확인할 숫자 M개 확인?
4.확인할 숫자
순서는 안 중요한데 개수가 중요 set안됨 이분탐색? 
'''
n=int(input())
nli=list(map(int,input().split()))
nli.sort()
m=int(input())
mli=list(map(int,input().split()))
li=[]

while True:
    start=0
    endp=max(nli)
    endm=min(nli)
    num=0
    for i in mli:
        if i>0:
            mid=(start+endp)//2
            while True:
                if i>mid:
                    start=mid+1
                    
            


# In[4]:


n=int(input())
nli=sorted(map(int,input().split()))
m=int(input())
mli=map(int,input().split())

def binary(l, nli, start, end):
    if start>end:
        return 0
    mid=(start+end)//2
    if l==nli[mid]:
        i,j=1,1
        while mid-i>=start:
            if nli[mid-i]!=nli[mid]:
                break
            else:
                i+=1
        while mid+j<=end:
            if nli[mid+j]!=nli[mid]:
                break
            else:
                j+=1
        return i+j-1
    elif l<nli[mid]:
        return binary(l, nli, start, mid-1)
    else:
        return binary(l, nli, m+1, end)
n_dic={}
for k in nli:
    start=0
    end=len(nli)-1
    if k not in n_dic:
        n_dic[n]=binary(k, nli, start, end)
print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in mli))


# In[ ]:




