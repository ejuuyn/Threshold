#3강 - 문법 기초
#3-1 matrix----

#matrix <-- 저장하는 자료의 종류 동일
#data frame <-- 숫자와 문자 등 섞어 저장 가능


z <- matrix(1:20, nrow=4, ncol=5) #nrow(number of row:행의 수), ncol(number of column:열의 수)
z

#matrix 생성 
z2 <- matrix(1:20, nrow=4, ncol=5, byrow=T)  #byrow : 행 방향으로  
z2

x <- 1:4
y <- 5:8

m1 <- cbind(x,y)  #column bind : 열 방향 결합
m2 <- rbind(x,y)  #row bind : 행 방향 결합
m1
m2

m3 <- rbind(m2,x)
m4 <- cbind(z,x)
m3
m4


#matrix안 에서의 위치 지정 -- index
z[2,3]  #2행 3열에 있는 값 : [행,열]
z[1,4]
z[2,]
z[,4]

#행과 열에 이름 붙이기
rownames(z)  #rownaems() : 행의 이름
colnames(z)  #colnaems() : 열의 이름 

rownames(z) <- c("row1","row2","row3","row4")
colnames(z) <- c("col1","col2","col3","col4","col5")
z

#행,열 이름으로 데이터 접근하기
z[,"col3"]
z["row2",]



#3-2 data frame----

city <- c("Seoul","Tokyo", "Washington")
rank <- c(1,3,2)
city.info <- data.frame(city,rank)

city.info[3,1]
city.info[2,]
city.info[,1]

is.data.frame(iris)     #객체가 data.frame인지 아닌지 확인
iris[,"Species"]        #결과가 vector ,iris[,5]와 동일 
iris["Species"]         #결과가 150x1 data frame
iris$Species            #결과가 vector (matrix에서는 잘 안됨)


iris[,c(1:2)]                      #앞의 2개 컬럼 데이터 보기
iris[,c(1,3,5)]                    
iris[,c("Sepal.Length","Species")] 
iris[1:50,]                        
iris[1:50,c(1,3)]                  



#3-3 matrix, data frame 다루기----
dim(iris)   #행과 열의 수 보이기
nrow(iris)  #행의 수 보이기
ncol(iris)  #열의 수 보이기
names(iris) #컬럼이름 보이기,colnames()와 동일
head(iris)  #데이터셋의 앞부분 일부 보기
tail(iris)  #데이터셋의 뒷부분 일부 보기

iris

str(iris)  #데이터셋 요약 보기

unique(iris[,5])  #종의 종류(중복제거) : 3개 품종

table(iris[,"Species"])  #도수분포표 작성 : 종별개수 count

#행과 열의 합계와 평균

colSums(iris[,-5])     #열별 합계
colMeans(iris[,-5])    #열별 평균
rowSums(iris[,-5])     #행별 합계
rowMeans(iris[,-5])    #행별 평균


#행과 열 변환(transpose) 하기  <- t()

z <- matrix(1:20, nrow=4, ncol=5)
z
t(z)
t(iris)


#subset()함수 : 조건에 맞는 행(row) 추출

IR.1 <- subset(iris, Species=="setosa")   #iris dataset에서 품종이 setosa인 행만 뽑아서 IR에 저장
                      #조건절(매개변수)
IR.1
IR.2 <- subset(iris, Sepal.Length>5.0 &
                     Sepal.Width>4.0)
IR.2


#matrix간에도 사칙연산 가능(행/열의 수가 동일할 때)
a <- matrix(1:20,4,5)
b <- matrix(21:40, 4,5)
a
b
a
b
a+b
b-a
b/a
a*b

3*a
b-5
2*a-3*b

a <- a*3
b <- b-5
a
b


#matrix와 data frame을 구분하는 함수

class(iris)
class(state.x77)
is.matrix(iris)
is.data.frame(iris)

#data frame to matrix
iris.m <- as.matrix(iris[,1:4]) 
head(iris.m)
tail(iris.m)

#matrix to data frame
st <- data.frame(state.x77)
head(st)
tail(st)


tmp <- iris[,-5]
class(tmp)
tmp2 <- as.matrix(tmp)
class(tmp2)


#3-4 파일에서 데이터 읽어오기/쓰기----

setwd("c:/Rworks")       #파일이 있는 폴더 지정
mydata <- read.csv("test.csv"    #절대경로를 입력하여 파일선택
                   ,header = True)
mydata                   #전체 데이터 출력

head(mydata)             #앞의 몇 줄 데이터 출력
tail(mydata)             #뒤의 몇 줄 데이터 출력

mydata[2,3]              #2행 3열의 원소값 출력
nrow(mydata)             #행의 개수 출력
ncol(mydata)             #열의 개수 출력
dim(mydata)              #행,열의 개수 출력

myRow1 <- mydata[2,]     #2행의 값 추출, 벡터생성
myRow2 <- mydatd[,3]     #3열의 값 추출, 벡터생성

mynew <- Mydata[,c(2,3)] #2,3열만 추출
write.csv(mynew, "kid_new.csv",
          row.names=F, quote=F)
 
mydata <- read.csv(file.choose(),    #파일탐색기 열기_파일탐색기능
                   header = True)   


#read.csv 실행 시 한글 깨짐 해결
#R에서 파일 읽을 때 encoding 옵션 추가
setwd("c:/Rworks")
mydata <- read.csv("test.csv",header=TRUE,
                   encoding="utf-8")  


#3-5 list, factor ----

#list : 벡터와 비슷하나 벡터와 달리 여러 자료형의 데이터를 섞어서 저장할 수 있음

member <- list(name='kim',address='pusan',
               tel='010-1234-5678', age=20, married=FALSE)
member

member[[3]]      #list에서 요소값을 불러올때 [[]]
member$name
member$address


#factor
blood.vec <- c("A","A","AB","O","B")
blood.vec
blood.type <- factor(c("A","A","AB","O","B"))
blood.type
is.factor(blood.type)

blood.type <- factor(c("A","A","AB","O","B"))
blood.type[6] <- "D"


blood.type
as.numeric(blood.type)        #as.numeric - 숫자로 치환하라.
levels(blood.type)
levels(blood.type)[2]


#3-L R tips ----
#패키지 설치
#install package

library(ggplot2)

scatter <- ggplot(data=iris, aes(x=Sepal.Length, y=Sepal.Width)
scatter + geom_point(aes(color+Species, shape=Species))+
  xlab("Sepal Length")+ ylab("Sepal Width")+
  ggtitle("Sepal Length-Width")

View(iris)
