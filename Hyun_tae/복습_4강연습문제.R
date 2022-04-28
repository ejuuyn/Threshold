# matrix와 data frame는 2차원 데이터를 저장
# vector는 1차원 데이터를 저장히기 위한 자료구조
# data.frame 열 데이터 뽑는 방법
# 


#과제 4-1
edu <- infert[,"education"]
edu
table(edu)
unique(infert[,"education"])    #폼의 종류 보기(중복제거)
table(edu)
is.vector(edu)
barplot(table(edu),
        main="Education",
        xlab="#of education",
        ylab="edu")

#과제 4-2
score <- c(90,85,73,80,85,65,78,50,68,96)
names(score) <- c("KOR","ENG","MATH","HIST","SOC","MUSIC","BIO","EARTH","PHY","ART")
score
# 평균
(score)
# 중앙값
median(score)
# 표준편차
sd(score)
#성적이 높은 과목(최대값)
score[score == max(score)] #몰?루
subset(score, score == max(score))
#boxplot, 이상치 제시
boxplot(score)
#성적 히스토그램, 타이틀 Hong's score, 막대색: 보라색
hist(score,
     main="Hong's score",
     xlab="subject",
     ylab="score",
     col="purple",
     breaks=5)

#과제 4-3
mtcars
head(mtcars)
require(graphics)
mean(mtcars$wt)
median(mtcars$wt)
mean(mtcars$wt, trim = .15)
sd(mtcars$wt)

summary(mtcars$wt)

t <- table(mtcars$cyl)
barplot(t)

#한번에 두개
par(mfrow=c(1,1))
hist(mtcars$wt)
barplot(table(mtcars$cyl), main = "barplot of mtcars$cyl")
barplot(table(mtcars$gear), main = "barplot of mtcars$gear")

par(mfrow=c(1,1))
boxplot(mtcars$wt)

boxplot(mtcars$disp)
summary(mtcars$disp)
