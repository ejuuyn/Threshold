# 데이터 스케일링(표준화와 정규화)
# 데이터 스케일링: 데이터들의 범위가 같아지도록 속성(변수)별로 값을 비례적으로 조정하는 과정을 의미함.
# 표준화와 min-max 정규화가 많이 사용되며, 변수들의 측정단위나 값의 범위가 다를 때 표준화 혹은 정규화를 적용하여 같은 기준으로 데이터 파악 가능

# 1.표준화: 각 개체들이 평균을 기준으로 얼마나 떨어져 있는지를 나타내는 값으로 변환하는 과정
 # 표준화한 후 특정 범위를 벗어난 데이터를 확인하여 이상치 판별에 활용 가능
# 1-1. 함수: scale(데이터, center = TRUE, scale = TRUE)
             # center: TRUE면 데이터에서 해당 벡터의 평균을 뺌
             # scale: center=TRUE, sclae=TRUE --> 데이터를 해당 벡터의 표준편차로 나눔
             #        center=FALSE, scale=TRUE --> 데이터를 해당 벡터의 제곱평균제곱근(RMS)으로 나눔
             #        scale=FALSE --> 데이터를 어떤 값으로도 나누지 않음


data("mtcars")
str(mtcars)

test.cars <- mtcars[,c("mpg","hp")]
# mpg, hp 변수로만 이루어진 데이터프레임 생성
# 아래와 결과 동일
library(dplyr)
data.frame(mtcars) %>%
  select(mpg, hp)

head(test.cars)

# 표준화한 변수 추가
test.cars <- transform(test.cars,
                       mpg_scale = scale(test.cars$mpg),
                       hp_scale = scale(test.cars$hp))
head(test.cars)




# 2. 정규화: 데이터의 범위를 0과 1 사이로 변환하여 데이터의 분포를 조정하는 방법
 # 데이터군 내에서 특정 개체가 가지는 위치를 파악하고 비교할 때 사용

Min <- min(iris$Sepal.Length)
Max <- max(iris$Sepal.Length)

iris$SL_nes <- scale(iris$Sepal.Length, center = Min, scale = Max-Min)

head(iris)
