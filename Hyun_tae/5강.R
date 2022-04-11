iris.2 <- iris[,3:4]
point <- as.numeric(iris$Species)
color <- c("red", "green","blue")
plot(iris.2,
     main="Iris plot",
     pch=c(point),
     col=color[point])





beers=c(5,2,9,8,3,7,3,5,3,5)
bal=c(0.1,0.03,0.19,0.12,0.04,0.0095,0.97,0.06,0.02,0.05)
tbl <- data.frame(cbind(beers,bal))
tbl;class(tbl)
plot(bal~beers,data=tbl)
res=lm(bal~beers,data=tbl)

#상관분석
cor(iris[,1:4])

#iris의 실제
str(iris)
class(iris)
dim(iris)
head(iris)
table(iris$Speices)
summary(iris)
sd(iris[,1])

par(mfrow=c(2,2))
boxplot(Sepal.Length~Species, data = iris,
        main = "Sepal.Length")

point <- as.numeric(iris$Species)
color <- c("red","green","blue")
pairs(iris[,-5],
      pch=c(point),
      col=color[iris[,5]])
