#4장
#4-1 기초 통계 개념
#4-2 일변량 질적 자료 분석----

ans=c("Y","Y","N","Y","Y")
table(ans)                      # 도수분포표 출력
table(ans)/length(ans)          # 비율 출력 

iris$Species                    # ==iris[,5]
table(iris$Species)

favorite.color <- c("red","green","yellow",
                    "red","green","red","red")
sum <- table(favorite.color)    #도수분포표
sum
barplot(sum,main="Favorite.color")

#한페이지에 여러 그래프

par(mfrow=c(1,3))   #1x3윈도우 생성
barplot(table(mtcars$carb),
        main="Barplot of Carburetors",
        xlab="#of carburetors",
        ylab="frequency",
        col="blue")
barplot(table(mtcars$cyl),
        main="Barplot of Cylender",
        xlab="#of cylender",
        ylab="frequency",
        col="red")
barplot(table(mtcars$gear),
        main="Barplot of Grar",
        xlab="#of gears",
        ylab="frequency",
        col="green")


#원그래프 작성

favorite.color <- c("red","green","yellow",
                    "red","green","red","red")
sum <- table(favorite.color)    #도수분포표
pie(sum, main="Favorite color")


#4-3 일변량 양적 자료의 분석 ----

mydata=c(50,60,100,75,200)
mydata.big = c(mydata, 50000)
mean(mydata)                    # 평 균
mean(mydata.big)
median(mydata)                  # 중 앙 값
median(mydata.big)
mean(mydata,trim=0.2)           # 절 사 평 균
mean(mydata.big, trim=0.2)
quantile(mydata)                # 사 분 위 수
quantile(mydata,(0:10)/10)
summary(mydata)
fivenum(mydata)                 # quantile()과 비슷

#최대값/최솟값, 분산,표준편차
diff(range(mydata))    # 최대값 - 최솟값
var(mydata)            # 분산
sd(mydata)             # 표준편차

#박스플롯
#state.x77이용

head(state.x77)

#iris를 이용하 boxplot

boxplot(iris$Petal.Width,
        ylab="Petal.Width")

boxplot(Petal.Width~Species,data=iris,
        ylab="Petal.Width")


#히스토그램----

st.income <- state.x77[,"Income"]
hist(st.income,
     main="Histogram for Income",
     xlab="income",
     ylab="frequency",
     border="blue",
     col="green",
     las=2,
     breaks=5)    #break:막대의개수
                   #break 수가 작으면 넓게 자르는 것

#줄기 - 잎 - 그림
score <- c(40,55,90,75,59,60,63,65,69,71)
stem(score,scale=2)

#4-4 R tip

#paste()함수 : 여러 문자열을 연걸하여 하나로 만들 때 사용
paste("Good","Morning","Tom",sep=" ")
paste("Good","Morning","Tom",sep="/")
paste(1:10,"is good", sep=" ")


#str 함수
#substr() : Substirng의 약자, 문자열 가르기
#nchar() : number of character, 문자열의 길이

str <- "Good Morning"
substr(str,1,4)
substr(str,6,nchar(str))

#gsub() : 문자열 바꾸기
gsub("Good","nice",str)
str <- gsub(" ","/", str)
str
