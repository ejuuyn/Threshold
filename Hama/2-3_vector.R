#변수에는 벡터를 저장.
#벡터 1차원자료의 배열을 저장할 수 있음
#벡터를 저장할 때는 c라는 함수.

x <- c(1,2,3)                               # 숫자형 벡터
y <- c("a","B","c")                         # 문자형 벡터
z <- c(TRUE,TRUE,FALSE,TRUE)                # 논리형 벡터


x
y

w <- c(1,2,3,"a","b","c")
w

x <- c(1,2,3)
z <- c("a","b","c")

z

#연속되는 값이 반드시 동일한 타입이어야 함.

v1 <- 50:90
v1

v2 <- c(1,2,5, 50:90)
v2

#seq -- 일정한 간격의 숫자로 구성된 벡터
#(시작, 종료, 간격)
v3 <- seq(1,101,3)
v3

v4 <- seq(0.1,1.0,0.1)
v4

#rep <- 어떠한 한 값 반복해서 저장할 때 사용
#(반복값, times = 횟수)
v5 <- rep(1,times = 5)
v5

v6 <- rep(1:5,times=3)
v6

v7 <- rep(c("a","b","c"),each=3)    #앞의 벡터를 각각 반복(each)
v7

v8 <- rep(c("a","b","c"),times=3)
v8

#names <- 벡터 여러개의 연속된 값에 이름을 붙임

score <- c(90,85,70)     #성적
names(score) <- c("John","Tom","Jane")

score
names(score)[2] #[n] <- 몇 번째 거를 가져와라
names(score)[1]


d <- c(1,4,3,7,8) #[n] <- index (색인을 붙이는 것.)
d[1]
d[2]
d[5]

d[1:3]
d[c(1,3,5)]
d[seq(1,5,2)]


#negative index
#인덱스 안에 마이너스 <-  이거 제외하고 전부 다.
d <- c(1,4,3,7,8)
d[-2]                       #두번 째 값은 제외하고.
d[-c(3:5)]                  #세번 쨰에서 다섯번 째 값은 제외하고.

#이름으로 값 추출하기
GNP <- c(2090,2450,960)
names(GNP) <- c("Korea","Japan","Nepal")
GNP[1]
GNP["Korea"]
GNP[c("Korea","Nepal")]


#연습3

d <- 101:200
d


#2-3 벡터연산

d <- c(1,4,3,7,8)
2*d
d-5
3*d+4


x <- c(1,2,3)
y <- c(4,5)
c(x,y)
z <- c(x,y)
z


x <- c(1,2,3)
y <- c(4,5,6)
x+y
z <- x+y
z

#벡터에 적용 가능한 함수들
sum()            #자료의 합
mean()           #자료의 평균
median()         #자료의 중앙값 
max(), min()     #자료의 최대,최소값
var()            #자료의 분산 값
sd()             #자료의 표준편차
sort()           #자료를 정렬하여 출력
range()          #자료의 범위(최대값~최소값)
length()         #자료의 개수

d <- c(1,2,3,4,5,6,7,8,9,10)
sum(d)
sum(2*d)
length(d)

max(d)
min(d)
sort(d)
sort(d,decreasing=FALSE)
sort(d,increasing=FALSE)
sort(d,decreasing=TRUE)

v1 <- median(d)
v1
v2 <- sum(d)/length(d)
v2


v1 <- c(1,2,3,4,5,6,7,8,9,10)

sort(x = v1,decreasing = TRUE)
sort(v1,FALSE)
sort(v1)           #decreasing = FALSE

#논리연산자

d <- c(1,2,3,4,5,6,7,8,9)
d>=5
d[d>5]       #TRUE만 결과로 #6,7,8,9
sum(d>5)     #TRUE는 1, FALSE는 0으로 취급
sum(d[d>5])  #5보다 큰 값의 개수를 출력
             #FALSE,FALSE,FALSE,TRUE,TRUE,TRUE
             #TRUE인 값만 출력   #6,7,8,9
             #6+7+8+9

d==5

condi <- d>5 & d<8
d[condi]   #조건에 맞는 값들을 선택

?summary.aov

help(sum)
? sum

help("sum")

help.search("average")

history()

d <- 101:200

d
d[10]
d[-c(196:200)]

d <- 101:200

d

tail(d,10)

d[10]

d[91:100]

d[-c(1:90)]

d.20 <- d[1:20]
d.20

d[d %% 2 == 0]

d.20[-5]

d.20[-c(5,7,9)]

d1 <- 1:50
d2 <- 51:100

d1
d2

d1+d2

d2-d1

d1*d2

d2/d1

sum(d1)

sum(d2)

max(d1)

min(d2)

max(d2)

average(d2)

mean(d1)

mean(d2)

mean(d2) - mean(d1)

sort(d1, decreasing = TRUE)



