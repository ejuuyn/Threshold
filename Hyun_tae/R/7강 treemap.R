#7강 데이터 시각화
#treemap
install.packages("treemap")
library(treemap)
data("GNI2014") #어떤 패키지에 있는 이런 샘플 데이터를 가져올 떄 
                  #안쓸 경우도 있음_메뉴얼에 따라 다름

str(GNI2014)
treemap(GNI2014,
        index = c("continent","iso3"), #계층을 선언하는 매개변수, 제일 첫 번째 매개 변수가 우리가 그림을 그릴 그 데이터 대상 데이터 셋
        vSize="population",
        vColor="GNI", #vcolor -> 다른 색 대신 지정한 칼라 사용해라
        type="value",
        bg.labels = "yellow")
#이번엔 대륙별로
GNI2014$GNI.total <- GNI2014$population*GNI2014$GNI
  #GNI.total이 없을 때 이런식으로 설정하면 GNI.total이 새로 만들어진다
GNI2014.a <- aggregate(GNI2014[,4:6],
                       by=list(GNI2014$continent),sum)
#aggregate 컬럼 중에서 4~6번째까지의 컬럼에 있는 값을 그룹 지어 집계
GNI2014.a$GNI.percap <- GNI2014.a$GNI.total/GNI2014.a$population

treemap(GNI2014.a,
        index=c("Group.1"),
        vSize="population",
        vColor="GNI.percap",
        type="value",
        bg.labels = "yellow")

