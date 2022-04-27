#5장 다변량 자료의 탐색
#5-1 산점도 ----

wt <- mtcars$wt
mpg <- mtcars$mpg
plot(wt,mpg,                       #2개 변수 (x축,y축)
     main="Car weight-mpg",        #제목
     xlab="Car weight",            #x축 레이블
     ylab="Miles per Gallon",      #y축 레이블
     col="red",                    #point의 color
     pch=25)                       #point의 종류

#pairs 함수----
vars <- c("mpg","disp","drat","wt")     #대상 변수
target <- mtcars[,vars]            
pairs(target,                           #대상 데이터
      main="Multi plots")

#여러 데이터의 정보를 가지고 있을 떄
iris.2 <- iris[,3:4]                      #데이터
point <- as.numeric(iris$Species)         #포인트모양 
color <- c("red","green","blue")          #포인트컬러
plot(iris.2, 
     main="Iris plot",
     pch=c(point),
     col=color[point])



#5-2 상관분석 ----


beers=c(5,2,9,8,3,7,3,5,5,5)
bal=c(0.1,0.03,0.19,0.12,0.04,0.095,0.07,0.06,0.06,0.06)
tbl=data.frame(cbind(beers,bal))
tbl; class(tbl)
plot(bal~beers,data=tbl)   #산점도  #beers가 x축  #bal이 y축
res=lm(bal~beers,data=tbl) #회귀식
abline(res)                #회귀선 그리기
cor(beers,bal)             #상관성 분석시행


cor(iris[,1:4])


#선그래프

month=1:12
late=c(5,8,7,9,4,6,12,13,8,6,6,4)
plot(month,                   #x데이터  #시간데이터
     late,                    #y data   #지각생 데이터
     main="Late students",    #그래프제목
     type="l",                #그래프의 종류 선택(알파벳)
     lty=1,                   #그래프 선의 종류(line type) 선택
     lwd=1,                   #선의 굵기 선택
     xlab="Month",            #x축 레이블
     ylab="late cnt")         #y축 레이블

#여러개의 선그래프
month=1:12
late1 = c(5,8,7,9,4,6,12,13,8,6,6,4)
late2 = c(4,6,5,8,7,8,10,11,6,5,7,3)

plot(month,                #x data
     late1,                #y data
     main="Late students",
     type="b",             # 그래프의 종류 선택(알파벳)
     lty=1,                #선의 종류 선택
     col="red",            #선의 색깔 선택
     xlab="Month",         #x축의 레이블
     ylab="Late cnt"       #y축의 레이블
     )
lines(month,
      late2,
      type="b",
      col="blue")


#5-4 데이터 분석 사례-----

str(iris)    #데이터셋 일반 정보
class(iris)
head(iris)
dim(iris)
table(iris$Species)

summary(iris[,1])
summary(iris[,2])
summary(iris[,"Petal.Length"])
summary(iris$Petal.Width)
