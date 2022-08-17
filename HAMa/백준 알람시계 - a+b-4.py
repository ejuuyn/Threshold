#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 백준 2884 알람시계
h,m = map(int,input().split())
if m < 45 :   # 45분을 뺴게 되니까 h가 0일 때는 23으로 변경되어야함.
    if h == 0 :  # = : 할당연산자 / == : a=b (좌측데이터 = 우측데이터 )
        h = 23
        m += 60   # m += 60 --> m = m + 60
    else: 
        h -= 1    # h -= 1 --> h = h -1 
        m += 60   # m = m + 60
        
print(h,m-45)


# In[ ]:


# 백준 2908 상수
a,b = input().split()   # 왜 여기서 int가 들어가면 안됩니까?

a = int(a[::-1])  # [::-1] 역순
b = int(b[::-1])

print(a) if a>b else print(b)



# In[ ]:


# 백준 2920 음계
# sort 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬
# sort의 key옵션, 지정된 함수의 결과에 따라 정렬

a = list(map(int,input().split()))
result = [1,2,3,4,5,6,7,8]

if a == result:
    print ("ascending")
elif a == result[::-1]:  #elif : else if 
    print("descending")
else:
    print("mixed")
    
    


# In[ ]:


#백준 3052 나머지

arr = []
for i in range(10):
    n= int(input())
    arr.append(n%42)

arr = set(arr)
print(len(arr))


# In[ ]:


# 백준 8958 OX

a= int(input())
for i in range(a):
    b=input()
    s=list(b)
    sum=0
    c=1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c=1
    print (sum)


# In[ ]:


# 백준 8958 OX (2)

a= int(input())
                        #처음에 정수 a를 받고 이후 for 문을 a번 만큼 반복
for i in range(a):   
    b = list(input())  
    score = 0    #score 변수를 0으로 지정
    sum_score = 0   # 새로운 ox리스트를 입력받으면 점수 합계를 리셋.
    for ox in b:   
        if ox == 'O':
            score += 1   # 'O'가 연속되면 점수가 1씪 커짐
            sum_score += score
        else:
            score = 0
    print (sum_score)


# In[ ]:


#백준 9498 시험성적

a = int(input())

if a <= 100 and a >= 90:
    print ('A')


elif a <= 89 and a >= 80:
    print ('B')


elif a <= 79 and a >= 70:
    print ('C')
    
elif a <= 69 and a >= 60:
    print ('D')

else:
    print ('F')


# In[18]:


#백준 10171 고양이

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")



# In[23]:


#백준 10172 개

print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")


# In[ ]:


#백준 10809 알파벳 찾기

word = input()
alphabet =list(range(97,123)) #아스키코드 숫자범위(?) : a =97, z =122
#근데 왜 123까지 함>?

for i in alphabet :
    print(word.find(chr(i)))   #chr : 아스키 코드에 해당하는 숫자를 문자열로 변환


# In[ ]:


#백준 10809 알파벳 찾기(2)

X = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in X:    #index함수를 통해 X 위치의 알파벳을 반환
        print(X.index(i), end= ' ') #한 칸씩 띄어서 위치 반환 -->' '
    else:
        print( -1, end = ' ')   #존재하지 않는 알파벳을 -1 로 반환
        
        


# In[ ]:


#백준 10818 최소,최대 

a = int(input())     #정수의 개수 입력 받기
b = list(map(int,input().split()))   #정수 입력 받기+input().split()을 통해 공백으로 구분하기
max = b[0]   
min = b[0]    #각각 첫 번쨰 요소 넣어주기 

for i in b[1:]:    #b의 두번째 요소부터 마지막 요소까지 비교
    if i > max :
        max = i        #max보다 크면 max 값을 바꿔주고 
    elif i < min:
        min = i     #min 보다 작으면 min 값을 바꿔준다. 

        
print (min,max)



# In[ ]:


#백준 10818 최소,최대 (2)

a= int(input())
b = list(map(int,input().split()))
print(min(b),max(b))          #그냥 파이썬의 내장함수 min()/max()사용


# In[ ]:


#백준 10871 x보다 작은 수 

a, b = map(int, input().split())
c = list(map(int, input().split()))  #c에 입력되는 수를 list에 정수로

for i in range(a):
    if c[i] < b:
        print(c[i], end= " ")
         
         


# In[ ]:


#백준 10950 a+b-3
c=int(input())
for i in range(c):
    a,b = map(int,input().split())
    print (a+b)


# In[ ]:


#백준 10951 a+b - 4

#try, except 문
#try블록 수행 중 오류 시 except 블록이 수행 

#while : ~~까지 작업을 수행 Or break문을 통해 중지

while 1:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break


# In[ ]:


#백준 10951 a+b - 4

try:
    while 1:
        a,b = map(int,input().split())
        print (a+b)

except:
    exit()
    


# In[ ]:




