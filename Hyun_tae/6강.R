#if문
a <- 10
b <- 20
if (a>5 & b>5){
  print (a+b)
}
if (a>5 | b>30){
  print (a*b)
}

ifelse (a>b,c <- a,c <- b)



#반복문:for
for(i in 1:10){
  cat("2*",i,"=",2*i,"\n")
}

#for + if 구문
for(i in 1:20){
  if(i%%2==0){
        print(i)
  }
}

v1 <- 101:200
for(i in 1:length(v1)){
  if(v1[i]%%2==0) {
    print(v1[i]*2)
  } else {
    print(v1[i]+2)
  }
}

sum <- 0
for(i in 1:100){
  sum <- sum + i
}
print(sum)

#반복문:while
i <- 1
while(i<=10){
  print(i)
  i <-i+1
}

#예제

subset(iris, Sepal.Length >=5.0&
              Sepal.Length <=6.0)[,1:2]

idx <- c()
for (i in 1:nrow(iris)){
  if (iris[i, "Sepal.Length"] >=5.0 &
      iris[i,"Sepal.Length"] <=6.0) {
    idx <- c(idx,i)
  }
}
print(idx)
iris[idx,c("Sepal.Length","Sepal.Width")]

#사용자정의 함수

mymax <- function(x,y) {
  num.max <- x
  if(y>x) {
    num.max <- y
  }
  return(num.max)
}

mymax(19,15)

#default value

mydiv <- function(x,y=2) {
  result <- x/y
  return(result)
}
mydiv(x=10,y=3)
mydiv(10,3)
mydiv(10)

myfunc <- function(x,y) {
  val.sum <- x+y
  val.mul <- x*y
  return(list(sum=val.sum,mul=val.mul))
}
result <- myfunc(5,8)
result$sum
result$mul

#Apply 함수a
apply(iris[,1:4],2,mean)

apply(iris[,1:4],1,mean)

lapply(iris[,1:4],mean)

#sapply함수
sapply(iris[,1:4],mean) # 결과 벡터형식
sapply(iris[,1:4],mean,simplify=F) #결과 리스트 형식

#예제
n <- readline(prompt ="숫자를 입력하세요: ")
cat("입력한 숫자는", n ,"입니다. \n")

num <- round(runif(1)*100,digits=0)
guess <-  -1
cat("Guess a number between 0 and 100. \n")

while(guess !=num){
  guess <- readline(prompt="Guess number :")
  guess <- as.integer(guess)
  if (guess==num){
    cat("축하,", num, "맞음.\n")
  } else if (guess<num){
    cat("더 작음. \n")
  } else if(guess>num){
    cat("더 큼! \n")
  }
}
sd
apply
