vars <- c("mpg","disp","drat","wt")
target <- mtcars[,vars]
pairs(target,
      main="Multi plots")
