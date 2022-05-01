#6장 R프로그래밍
#6-1 if문----

a <- 10
if(a>5){
  print (a)
} else {
  print(a*10)
  print(a/10)
}


a <- 10
b <- 20
if (a>5 & b>5){     #and
  print (a+b)
}
if (a>5 | b>30){    #or
  print (a*b)
}


#ifelse
a <- 10
b <- 20
ifelse (a>b, c <- a, c <- b)
c

a <- 10
b <- 20
if(a>b){
  c <- a
} else {
  c <- b
}
c

#6-2 for,while 문----

#for문----
for(i in 1:10) {
  print(i)
}

for(i in 1:10){
  cat("2*",i,"=",2*i,"\n")
}

for(i in 1:20){
  if(i%%2==0){       #짝수인지 확인
    print(i)
  }
}


v1 <- 101:200
for(i in 1:length(v1)){
  if(v1[i]%%2==0) {
    print(v1[i]*2)
  }else {
    print(v1[i]+2)
  }
}


sum <- 0
for(i in 1:100){
  sum <- sum+i
}
print(sum)


#while 문----

i <- 1
while(i<=10) {
  print(i)
  i <- i+1
}

subset(iris,Sepal.Length >= 5.0 &        #subset : 행을 골라내라
         Sepal.Length <= 6.0)[,1:2]

idx <- c()                              #---> 아무것도없는 벡터  , i 의 반복을 주위깊게 볼 것
for (i in 1:nrow(iris)){                #-->i가 몇번 쨰 행인가
  if(iris[i, "Sepal.Length"]>=5.0 &
     iris[i, "Sepal.Length"] <= 6.0){
    idx <- c(idx,i)                     #---> i 의 값이 idx에 저장
  } 
}
print(idx)                              #행을 골라난 다음 열을 지정
iris[idx, c("Sepal.Length","Sepal.Width")]


#변수 초기화의 필요성

ss <- 0
for (i in 1:100){
  ss <- ss + i           #변수 ss에 ss+i를 입력하시오
}                        #error 발생 : ss값이 없어서
print(ss) 


#6-3 사용자정의 함수----

mymax <- function(x,y){
  num.max <- x
  if(y>x){
    num.max <- y
  }
  return(num.max)
}

mymax(10,15)
mymax(20,15)


#default value 지정

mydiv <- function(x,y=2){     #y=2 <-- 초기값
  result <-  x/y
  return(result)
}

mydiv(x=10,y=3)
mydiv(10,3)
mydiv(10)


myfunc <- function(x,y){
  val.sum <- x+y
  val.mul <- x*y
  return(list(sum=val.sum, mul=val.mul))   #return해야하는 값이 여려개<-list로
}

result <- myfunc(5,8)
result$sum
result$mul

#내가 정의한 함수가 저장된 파일 사용하기
mydiv <- function(x,y=2){
  result <- x/y
  return(result)
}

setwd("c:Rworks")   #myfunc.R이 저장된 폴더
source("myfunc.R")  #myfunc.R의 명령어 실행
#함수 사용
a <- mydiv(20,4)
b <- mydiv(30,4)
a+b
mydiv(mydiv(20,2),5)


#6-4 appy계열 함수----

#r사용 시 while.for 권장하지 않음.
#--> apply 함수 사용

for(i in 1:4){
  print(mean(iris[,i]))
}

apply(iris[,1:4],2,mean)    #열 방향 작업
apply(iris[,1:4],1,mean)    #행 방향 작업 

#lapply <-  괄과가 list format
lapply(iris[,1:4],mean)     #컬럼방향  열방향

abc <- list(mtcars[,1],mtcars[,2],mtcars[,3],mtcars[,4])
lapply(abc,mean)
lapply(abc,mean)[[1]]


#sapply 실행결과를 벡터, 리스트로 선택
sapply(iris[,1:4],mean)               #결과가 Vector
sapply(iris[,1:4],mean,simplify=F)    #결과가 list

myfunc <- function(x){
  a <- max(x)
  b <- min(x)
  return(a-b)
}

sapply(iris[,1:4],myfunc)


#6-5 프로그래밍 예제

n <- readline(prompt="숫자를 입력하세요:")
cat("입력한 숫자는", n, "입니다.\n")

# 숫자 맞추기 게임.
num <- round(runif(1)*100,digits=0)
guess <- -1
cat("Guess a number between 0 and 100.\n")

while(guess !=num){
  guess <- readline(prompt="Guess number :")
  guess <- as.integer(guess)
  if (guess == num){
    cat("Congratulations," ,num, "is right.\n")
  } else if (guess < num){
    cat("It`s smaller!\n")
  } else if (guess > num){
    cat("It`s bigger!\n")
  }
}

#6 R tips -----
#함수의 코드가 궁금할 때 
#함수이름만 쳐보기

sd
sum
sink
