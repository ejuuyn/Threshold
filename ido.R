2+3
5-1
(3/6)*8
log(10)+5
log(2)
sqrt(25)
sqrt(49)
max(5,3)
a<-10
b<-20
c<-a+b
c
d<-10; e<-20; f<-15; g<-d+f+e; g
print(a+d)
v1 <- "good morning!"
print(v1)
v1 <- good morning!
print(v1)
A <- 10
B <- "good"
c <- NULL
d <- TRUE
c
d
x <- c(1,2,3)
z <- c("a","b","c")
print(x)
x
v1 <- 50:90
v1
v2 <- c(1,2,3,50:90)
v2
v3 <- seq(1,101,3)
v4 <- seq(0.1,1.0,0.1)
v3
v4
v5 <- rep(1, times = 5) 
v6 <- rep(1:5, times = 3)
v7 <- rep(c("a","b","c"), each = 3)
v8 <- rep(c("a","b","c"), times = 3)
v5
v6
v7
v8
score <- c(90,85,70)
names(score) <- c("john","tom","jane")
score
d <- c(1,4,3,7,8)
d[2]
d[1:3]
d[c(1,3,5)]
d[seq(1,5,2)]
d <- c(1,4,3,7,8,9)
d <- [-2]
d[-2]
d[-c(3:5)]
GNP <- c(3090,3450,960)
names(GNP) <- c("korea","japan","nepal")
GNP[1]
GNP["Korea"]
GNP[c("korea","nepal")]
GNP["korea"]
d <- 100:200
d
d[10]
d[-c(191:200)]
d[seq(100,200,2)]
d[seq(100,200,2)]
d.20 <- c(120:200)
d.20
d.20[-5]
d.20[-c(5,7,9)]
2*d
d <- c(1,4,3,7,8)
2*d
d-5
3*d+4
x <- c(1,2,3)
y <- c(4,5)
c(x,y)
z <- c(x,y)
y <- c(4,5,6)
x+y
z <- x+y
z
d <- c(1,2,3,4,5,6,7,8,9,10)
sum(d)
sum(2*d)
length(d)
mean(d[1:5])
max(d)
min(d)
sort(d)
sort(d, decreasing=FALSE)
sort(d, decreasing=TRUE)
v1 <- median(d)
v1
v2 <- sum(d)/length(d)
v2
v1 <- c(4,2,3,1,6,1,8,9)
sort(x=v1, decreasing+TRUE)
sort(x=v1, decreasing=TRUE)
sort(v1,FALSE)
d1 <- 1:50; d2 <- 51:100 
d1; d2
d1+d2; d2-d1; d1*d2
d2/d1
max(d2); min(d2)
median(d2)-median(d1)
mean(d2)-mean(d1)
sort(d1, decreasing=TRUE)
d3 <- c(d1(41:50), d2(91:100))
x <- d1[41:50]
y <- d2[91:100]
d3 <- c(x,y)
d3
y
d <- c(1,2,3,4,5,6,7,8,9)
d>=5
d[d>5]
sum(d>5)
sum(d[d>5])
d==5
condi <- d>5&d<8
condi
d[condi]
v1 <- 51:90
v1<60
v1[v1<60]
sum(v1<70)
sum(v1[v1>65])
v1[60:73]
condi <- v1>60 & v1 <73
v1[condi]
condi1 <- v1<65 | v1>80
v1[condi1]
condi2 <- v1/7
v1[condi2]
z <- matrix(1:20, nrow=4, ncol=5, byrow=T)
z
x <- 1:4
y <- 5:8
m1 <- cbind(x,y)
m2 <- rbind(x,y)
m1
m2
m3 <- rbind(m2,x)
m4 <- cbind(z,x)
m3; m4
z[2,3]
z[1,4]
z[2,]
z[,4]
rownames(z) <- c("row1","row2","row3","row4")
colnames(z) <- c("col1","col2","col3","col4","col5")
z[,"col3"]
z["row2",]
m <- c(10, 40, 60, 20)
f <- c(21,60,70,30)
score <- cbind(m,f)
score
colnames(score) <- c("male","female")
score[2,]
score[,"female"]
score[3,"female"]

city <- c("seoul","tokyo","washington")
rank <- c(1,3,2)
city.info <- data.frame(city,rank)
city.info
iris
is.data.frame(iris)
iris[,"Species"]
iris["Species"]
iris$Species
iris[,c(1:2)]
iris[,c(1,3,5)]
iris[,c("Sepal.Length","Species")]
iris[1:50,]
iris[1:50,c(1,3)]
dim(iris)
nrow(iris)
ncol(iris)
names(iris)
head(iris)
tail(iris)
str(iris)
unique(iris[,5])
table(iris[,"Species"])
colSums(iris[,-5])
colMeans(iris[,-5])
rowSums(iris[,-5])
rowMeans(iris[,-5])
z <- matrix(1:20,nrow = 4,ncol = 5)
z
t(z)
IR.1 <- subset(iris, Species=="setosa")
IR.1
IR.2 <- subset(iris,Sepal.Length>5.0 & 
                    Sepal.Width>4.0)
IR.2
a <- matrix(1:20,4,5)
b <- matrix(21:40,4,5)
a;b;
a+b
b-a
b/a
a*b
3*a
b-5
2*a + 3*b
a <- a*3
b <- b-5
a
b
class(iris)
class(state.x77)
is.matrix(iris)
is.data.frame(iris)
iris.m <- as.matrix(iris[,1:4])
head(iris.m)
class(iris.m)
st <- data.frame(state.x77)
head(st)
class(st)
tmp <- iris[,-5]
class(tmp)
tmp2 <- as.matrix(tmp)
class(tmp2)

setwd("c:/Rworks")
mydata <- read.csv("test.csv", header=TRUE)
mydata

setwd("c:/Rworks")
mydata <- read.csv("test.csv", header=TRUE)
mydata <- read.csv(file.choose(), header = TRUE)

state.x77
prdata <- subset(state.x77, Income > 5000)
write.csv(mynew, "rich_state.csv")

member <- list(name='kim',address='pusan',tel='010-1234-5678',age=20,married=FALSE)
member

member[[1]]
member$name

blood.type <- factor(c("A", "B", "AB", "O"))
blood.type
is.factor(blood.type)
blood.type[6] <- "D"

blood.type
as.numeric(blood.type)


#install package
library(ggplot2)
scatter <- ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width))
scatter + geom_point(aes(color=Species, shape=Species)) +
  xlab("Sepal Length")+ylab("Sepal Width")+ggtitle("Sepal Length-Width")
View(iris)

ans=c("Y","Y","N","Y","Y")
table(ans)
table(ans)/length(ans)

favorite.color <- c("red", "green", "yellow", "red", "green", "red", "red")
sum <- table(favorite.color)
sum
barplot(sum, main = "Favorite color")


par(mfrow=c(1,3))
barplot(table(mtcars$carb),
        main="Barplot of Carburetors",
        xlab="#of Carburetors",
        ylab="frequency",
        col = "blue")
barplot(table(mtcars$cyl),
        main="Barplot of Cylender",
        xlab="#of Cylender",
        ylab="frequency",
        col = "red")
barplot(table(mtcars$gear),
        main="Barplot of gear",
        xlab="#of gear",
        ylab="frequency",
        col = "green")

favorite.color <- c("red","green", "yellow", "green", "red", "red","red")
sum <- table(favorite.color)
pie(sum, main = "Favorite color")





























