setwd("")
hr <- fread("MFG10YearTerminationData.csv") %>%
as_tibble()

#전처리
#-1 컬럼명 변경
hr_adj <- hr %>%
  rename(id=EmployeeID,
        record_dt=recorddate_key,
        birth_dt=birthdate_key,
        hire_dt=orighiredate_key,
        trmt_dt=terminationdate_key,
        age=age,
        tenure=length_of_service,
        city=city_name,
        depart=department_name,
        job=job_title,
        store=store_name,
        gender=gender_short,
        gender_1=gender_full,
        reason=termreason_desc,
        type=termtype_desc,
        year=STATUS_YEAR,
        status= STATUS,
        unit=BUSINESS_UNIT) %>%
  
select(-record_dt, -gender_1, -birth_dt) %>%  
  
  mutate(hire_dt=hire_dt %>% mdy(),
         trmt_dt=trmt_dt %>% mdy(),
         id=id %>% as.character(),
         city=city %>% str_to_lower(),
         depart=depart %>% str_to_lower(),
         job=job %>% str_to_lower(),
         store=store %>% str_to_lower(),
         gender=gender %>% str_to_lower(),
         reason=reason %>% str_to_lower(),
         type=type %>% str_to_lower(),
         status = status %>% str_to_lower(),
         unit = unit %>% str_to_lower()) %>%
  
  select(id, year, status, reason, type, hire_dt, trmt_dt, tenure,age,gender,depart, store, job, store)
install.packages("lubridate")
library(lubridate)
install.packages("clipr")
library(clipr)

hr_adj %>%
  filter(id %>% is.na)

hr_adj %>%
  sum(is.na())
