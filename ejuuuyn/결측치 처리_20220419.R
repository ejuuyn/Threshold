# 1. 결측치 인식

# 1-1. is.na(): 데이터의 요소가 NA일 경우 TRUE, 그렇지 않을 경우 FALSE 반환
  # is.na()의 결과는 논리값이므로 산술계산 가능. TRUE를 1로 인식하기 때문에 is.na()를 적용한 후 합을 구하면 결측치의 개수 파악 가능

is.na(airquality$Ozone)
sum(is.na(airquality$Ozone))
table(is.na(airquality$Ozone))
 # table(): 범주별 도수를 구하는 함수


# 1-2. complete.cases(): 해당 데이터가 결측치를 갖고 있지 않은 완전한 데이터인지 묻는 함수. 데이터에 결측치가 없으면 TRUE, 있으면 FALSE 반환
  # 여러 변수들 중 na값이 하나라도 존재하는 행은 FALSE를 반환하므로 na값이 하나라도 존재하는 행을 찾을 때 편리함
  # complete.caseS()의 결과 역시 논리값이므로 합을 구하거나 도수분포표를 생성하여 결측치의 개수 파악 가능

air_na <- airquality[!complete.cases(airquality),]
 # na 값이 하나라도 존재하는 행들은 air_na 변수에 저장 - complete.cases함수를 적용했을 때 FALSE를 반환하는 행들만 저장하면 됨
head(air_na)

air_com <- airquality[complete.cases(airquality),]
head(air_com)



# 2. 결측치 처리

# 2-1. 결측치 제거
# 2-1-1. 결측치가 존재하는 행 제거
 # 데이터명[!is.na(데이터명),]
 # 데이터명[comlete.cases(데이터명),]
 # 데이터명 %>% filter(!is.na(데이터명))
 # na.omit(데이터명)

# 2-2. 평균대치법
airquality$Ozone <- ifelse(is.na(airquality$Ozone), mean(airquality$Ozone, na.rm = T), airquality$Ozone)
 # ifelse 함수를 이용해 Ozone 변수값이 na이면 평균으로 대체하고 na가 아니면 기존값을 그대로 가지게 함
table(is.na(airquality$Ozone))

