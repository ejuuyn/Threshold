# R을 이용한 표본 추출

# 1. 단순 임의 추출
 # sample(x, size, replace=FALSE, prop=NULL)
  # size: 표본의 크기
  # replace: 복원 추출 여부
  # prop: 데이터를 추출할 때의 가중치 지정
   # ex) prob=c(2,4,6): 첫 번째 데이터 뽑힐 확률 20%, 두 번째 40%, ...

# 1-1. iris 데이터 행의 개수에 70%에 해당하는 행번호를 랜덤으로 추출
idx <- sample(1:nrow(iris), nrow(iris)*0.7, replace=FALSE)

# 1-2. 추출한 행번호를 이용하여 training 데이터와 test 데이터 생성
training <- iris[idx,]
test <- iris[-idx,]

# 1-3. 데이터의 개수 확인
dim(iris)  # 행의 개수
dim(training)  # iris 행 개수의 70%에 해당하는 개수
dim(test)  # iris 행 개수의 30%에 해당하는 개수


# 2. 층화 임의 추출
 # strata(data, stratanames=NULL, size, method=c("srswor","srswr","poisson","sysatematic"), pik, description=FALSE)
  # stratanames: 데이터에서 계층(집단)을 구분하는 변수들 (여러개일 경우 c()안에 나열)
  # size: 각 계층에서 추출할 데이터의 개수
  # method: 데이터를 뽑는 방법 / srswor: 비복원 단순임의추출 / srswr: 복원 단순임의추출 / poisson: 포아송 추출 / systematic: 계통 추출
  # pik: 데이터를 표본에 포함시킬 확률
  # description: 표본크기와 모집단크기를 추출할지 여부 (TRUE/FALSE)
 # getdata(data, m): 표본 추출을 통해 얻어진 데이터 출력
  # data: 표본을 추출할 원본 데이터
  # m: 추출된 벡터 or 데이터 프레임

install.packages("sampling")
library(sampling)

# 2-1. 층화임의추출 수행한 후 sample 변수에 저장
sample <- strata(data=iris, c("Species"), size=c(20,15,15), method="srswor")

head(sample)

# 2-2. 추출된 데이터를 iris_sample 변수에 저장
iris_sample <- getdata(iris, sample)

head(iris_sample)

# 2-3. 표본 데이터의 Species 변수에 대한 도수분포표 생성
table(iris_sample$Species)
