library(dplyr)
library(data.table)
library(lubridate)
library(stringr)
library(clipr)

setwd()

hr <- fread("MFG10YearTerminationData.csv") %>%
  as_tibble()



# 1. 전처리
# 1-1. 컬럼명 변경
hr_adj <- hr %>% 
  rename(id = EmployeeID,
         record_dt = recorddate_key,
         birth_dt = birthdate_key,
         hire_dt = orighiredate_key,
         trmt_dt = terminationdate_key,
         age = age,
         tenure = length_of_service,
         city = city_name,
         depart= department_name,
         job = job_title,
         store = store_name,
         gender = gender_short,
         gender_1= gender_full,
         reason = termreason_desc,
         type = termtype_desc,
         year = STATUS_YEAR,
         status = STATUS,
         unit = BUSINESS_UNIT) %>% 
  select(-record_dt, -gender_1, -birth_dt) %>% 
  mutate(hire_dt = hire_dt %>% mdy(),
         trmt_dt = trmt_dt %>% mdy(),
         id = id %>% as.character(),
         # 문자형으로 변환
         city = city %>% str_to_lower(),
         # 투입한 변수의 값을 모두 소문자로 변환
         depart = depart %>% str_to_lower(),
         job = job %>% str_to_lower(),
         store = store %>% as.character(),
         gender = gender %>% str_to_lower(),
         reason = reason %>% str_to_lower(),
         type = type %>%  str_to_lower(),
         status = status %>% str_to_lower(),
         unit = unit %>% str_to_lower()) %>% 
  select(id, year, status, reason, type, 
         hire_dt, trmt_dt, tenure, age, gender, 
         depart, store, job, store, 
         city, unit) 




# 1-2. 변수 현황 파악
hr_adj %>%
  filter(id %>% is.na)

hr_adj %>%
  sum(is.na())

hr_adj %>%
  filter(id == '1318')

hr_adj %>%
  count(id, sort = T)

hr_adj %>%
  filter(year %>% is.na)

hr_adj %>%
  count(year, sort = T) %>% print(n=100)

hr_adj %>%
  distinct(id, year) %>%
  count(year)

hr_adj %>%
  count(status, sort = T) %>%
  print(n=100)

hr_adj %>%
  distinct(id, year, status) %>%
  count(year, status) %>%
  data.table()  %>%
  # status컬럼에 active, terminated 번갈아 출력되어 한 눈에 보기 어려움움
  dcast.data.table(year~status, value.var = "n") %>%
  # 위의 status 컬럼을 active컬럼, terminated컬럼으로 변경
  mutate(ter_prop = terminated/(active + terminated)) %>% round(3)
# status 중 terminated가 차지하는 비율 계산하여 '퇴사율'컬럼 생성

hr_adj %>%
  filter(reason %>% is.na)

hr_adj %>%
  count(reason) %>%
  print(n=500)

hr_adj %>%
  count(status, reason, year) %>%
  data.table() %>%
  # status, reason에 중복값 너무 많음
  dcast.data.table(status + reason ~ year, value.var = "n", fill = 0)
# status행, reason행, year열로 변경. 결측값은 0으로 출력

hr_adj %>%
  count(type) %>%
  print(n=100)
# 이거 왜 하는지 아직도 모르겠음..그냥 count에서 끝났을 때랑 결과 똑같은데

hr_adj %>%
  count(year, status, reason, type) %>%
  data.table() %>%
  dcast.data.table(status + reason + type ~ year, value.var = "n", fill = 0)

hr_adj %>%
  filter(hire_dt %>% is.na)

hr_adj %>%
  count(hire_dt)

hr_adj %>%
  mutate(hire_ym = hire_dt %>% str_sub(1,7),
         # hire_dt 문자열의 앞에서부터 1~7번째 문자로 hire_ym컬럼 생성
         hire_y = hire_dt %>% str_sub(1,4)) %>%
  count(hire_y, hire_ym)

hr_adj %>%
  mutate(hire_ym = hire_dt %>% str_sub(6,7),
         hire_y = hire_dt %>% str_sub(1,4)) %>%
  count(hire_y, hire_ym) %>%
  data.table() %>%
  dcast.data.table(hire_y ~ hire_ym, value.var = "n", sum) %>%
  as_tibble() %>%
  # tibble은 처음 10개 행과 모든 열만 출력, 각 열의 데이터 유형 표시
  print(n=100)

hr_adj %>%
  filter(trmt_dt %>% is.na)

hr_adj %>%
  count(trmt_dt)

hr_adj %>%
  filter(status != 'active') %>%
  # status가 active가 아닌 것에 한하여
  mutate(trmt_ym = trmt_dt %>% str_sub(6,7),
         trmt_y = trmt_dt %>% str_sub(1,4)) %>%
  # 퇴직년월, 퇴직년도 컬럼 생성
  count(trmt_y, trmt_ym) %>%
  data.table() %>%
  dcast.data.table(trmt_y ~ trmt_ym, value.var = "n", sum) %>%
  as_tibble()

hr_adj %>%
  filter(status != "active") %>%
  # status가 active가 아닌 것에 한하여
  mutate(trmt_ym = trmt_dt %>% str_sub(6,7),
         trmt_y = trmt_dt %>% str_sub(1,4)) %>%
  # 퇴직년월, 퇴직년도 컬럼 생성
  count(reason, trmt_y, trmt_ym) %>%
  data.table() %>%
  dcast.data.table(reason + trmt_y ~ trmt_ym, value.var = "n", sum) %>%
  as_tibble() %>%
  filter(trmt_y != '1900') %>%
  print(n=100)



# 2. 분석 기획

# 2-1. 평균 연차가 가장 높은 직군은 무엇인가?
# 2-1-1. 현재 재직 중인 직원별 연차 데모그래픽
emp_list <- hr_adj %>%
  arrange(id, year %>% desc, status %>% desc) %>%
  distinct(id,.keep_all = T) %>%
  # .keep_all = T: id 변수 필터링, 그 외 변수 유지
  select(id, reason, type, status, hire_dt, age, tenure, gender, depart, store, job, unit, city, year, trmt_dt) %>%
  arrange(id)

library(echarts4r)
emp_list %>%
  group_by(status) %>%
  e_chart() %>%
  e_density(tenure)

# 2-1-2. 연령별 근속연수
check_age <- emp_list %>%
  mutate(age_grp = ifelse(age < 20, '10s',
                          ifelse(age < 30, '20s',
                                 ifelse(age < 40, '30s',
                                        ifelse(age < 50, '40',
                                               ifelse(age < 60, '50s',
                                                      ifelse(age < 70, '60s', '70+'))))))) %>%
  summarise(avg = mean(tenure) %>% round(1),
            sd = sd(tenure) %>% round(1),
            n = n())


# 2-1-3. 성별 근속연수
check_gender <- emp_list %>%
  group_by(gender) %>%
  summarise(avg = mean(tenure) %>% round(1),
            sd = sd(tenure) %>% round(1),
            n = n())

emp_list %>%
  group_by(gender) %>%
  e_chart() %>%
  e_density(tenure)


# 2-1-4. 부서별 근속연수
check_depart <- emp_list %>%
  group_by(depart) %>%
  summarise(avg = mean(tenure),
            sd = sd(tenure),
            n = n()) %>%
  filter(n > 10) %>%
  arrange(avg %>% desc)

emp_list %>%
  group_by(depart) %>%
  e_chart() %>%
  e_boxplot(tenure) %>%
  # 왜 boxplot으로 볼까? --> 변수가 많아서인듯
  e_datazoom(x_index = 0, type = "slider")


# 2-1-5. 지점별 근속연수
check_store <- emp_list %>%
  group_by(store, unit) %>%
  summarise(avg = mean(tenure) %>% round(1),
            sd = sd(tenure) %>% round(1),
            n = n()) %>%
  filter(n > 10) %>%
  arrange(avg %>% desc)

emp_list %>%
  group_by(store) %>%
  summarise(tenure = mean(tenure)) %>%
  arrange(tenure %>% desc) %>%
  e_chart(store) %>%
  e_bar(tenure)



# 2-1-6. 직책별 근속연수
check_job <- emp_list %>%
  group_by(job) %>%
  summarise(avg = mean(tenure) %>% round(1),
            sd = sd(tenure) %>% round(1),
            n = n()) %>%
  filter(n > 10) %>%
  arrange(avg %>% desc)

emp_list %>%
  group_by(job) %>%
  e_chart() %>%
  e_boxplot(tenure) %>%
  e_datazoom(x_index = 0, type = "slider")



# 2-1-7. 거주지별 근속연수
check_city <- emp_list %>%
  group_by(city) %>%
  summarise(avg = mean(tenure) %>% round(1),
            sd = sd(tenure) %>% round(1),
            n = n()) %>%
  filter(n > 10) %>%
  arrange(avg %>% desc)


check_age %>% head(2)
check_city %>% head(2)
check_depart %>% head(2)
check_gender %>% head(2)
check_job %>% head(2)
check_store %>% head(2)


emp_list %>%
  group_by(gender, depart, job) %>%
  summarise(avg = mean(tenure),
            n = n()) %>%
  filter(n > 10) %>%
  arrange(avg %>% desc)





# 2-2. 퇴사 시점 분석
install.packages("DT")
library(DT)
# DT 패키지: DataTalbes 라이브러리를 통해 R 데이터를 보여주기 위한 datatable() 함수 제공
# R의 matrix와 dataframe에서 HTML 형식의 테이블 작성
bind_cols(hr_adj %>%
            arrange(id, trmt_dt %>% desc) %>%
            # id 오름차순, trmt_dt 내림차순 정렬
            distinct(id, .keep_all = T) %>%
            # id 중복값 제거, 그 외 변수 유지
            filter(trmt_dt != '1900-01-01') %>%
            # trmt_dt가 '1900-01-01'이 아닌 값만 선정
            mutate(trmt_year = trmt_dt %>% str_sub(1,4),
                   trmt_month = trmt_dt %>% str_sub(6,7)) %>%
            # 퇴사연도, 퇴사월 컬럼 생성
            group_by(trmt_year, trmt_month) %>%
            # 퇴사연도, 퇴사월 그룹화
            summarise(n = n()) %>%
            data.table() %>%
            dcast(trmt_year ~ trmt_month, value.var = "n", sum, fill = 0),
          hr_adj %>%
            group_by(year) %>%
            summarise(total_n = n())) %>%
  select(-year) %>%
  datatable()
# bind_cols(): 둘 이상의 데이터 프레임을 열 기준으로 합칠 때 사용(dataframe 1 + dataframe 2 + ...) / "base"패키지의 cbind()함수와 유사한 기능 수행
# bind_rows(): 둘 이상의 데이터 프레임을 행 기준으로 합칠 때 사용 / "base"패키지의 rbind()함수와 유사한 기능 수행


# 2-2-1. 퇴사하는 시점은 주로 언제인가?
hr_adj %>%
  arrange(id, trmt_dt %>% desc) %>%
  distinct(id, .keep_all = T) %>%
  filter(trmt_dt != '1900-01-01') %>%
  mutate(trmt_year = trmt_dt %>% str_sub(1,4),
         trmt_month = trmt_dt %>% str_sub(6,7)) %>%
  group_by(trmt_year, trmt_month) %>%
  summarise(n = n()) %>%
  arrange(n %>% desc)  # 강의안에서는 정렬 안 했지만, 내림차순으로 정렬하는 게 좋을 듯


# 2-2-2. 사유별 퇴사는 어떠한가?
emp_list %>%
  filter(status != 'active') %>%
  # = filter(status == 'terminated')
  mutate(trmt_year = trmt_dt %>% str_sub(1,4)) %>%
  group_by(reason, type, trmt_year) %>%
  summarise(n = n()) %>%
  data.table() %>%
  dcast.data.table(reason + type ~ trmt_year, value.var = "n", fill = 0) %>%
  # 사유별 해당 연도가 없을 수 있으니까 fill = 0 입력
  summarise(n = n()) %>%
  data.table()


# 2-2-3. 해고된 사원은 주로 어떤 부서 및 직급인가?
emp_list %>%
  filter(status != 'active') %>%
  mutate(trmt_year = trmt_dt %>% str_sub(1,4)) %>%
  # 이건 왜 만든 거지?
  filter(reason == 'layoff') %>%
  group_by(trmt_year, reason, type, depart, job) %>%
  datatable()



# 2-2-4. 연도별 자발적 퇴사의 비율이 높은 부서는 어디인가?
emp_list %>%
  filter(reason == 'resignation') %>%
  mutate(trmt_year = trmt_dt %>% str_sub(1,4)) %>%
  group_by(year, depart, job) %>%
  summarise(n = n()) %>%
  data.table() %>%
  dcast.data.table(depart + job ~ year, value.var = "n", sum)


