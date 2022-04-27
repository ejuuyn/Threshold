# t-검정

# 1. 일표본 t-검정
# 1-1. t검정 수행 전, 정규성 검정 필요 - 주로 샤피로-윌크 검정 사용: shapito.test(data)
# MASS 패키지의 cats 데이터 사용
library(MASS)
str(cats)

# 고양이 몸무게(Bwt) 변수에 대한 정규성 검정
shapiro.test(cats$Bwt)

# 데이터가 정규성을 만족한 경우, t.test() 함수 이용하여 일표본 t 검정 수행
 # t.test(x, alternative=c("two.sided","less","greater"), mu=0)
  # 양측검정: two.sided
  # 단측검정: less(표본평균이 특정 값보다 작은지) / greater(표본평균이 특정 값보다 큰지)
# 데이터가 정규성을 만족하지 않는 경우, wilcox.test() 함수 이용하여 t검정 수행
 # wilcox.test(x, alternative=c("two.sided","less","greater"), mu=0)

# 데이터가 정규성을 만족하지 않으므로 wilcox.test() 이용
wilcox.test(cats$Bwt, alternative = "two.sided", mu=2.6)




# 2. 대응표본 t-검정
# 함수: t.test(x, y, alternative=c("two.sided", "less", "greater"), paired=FALSE, m=0)
 # x, y: 처리방법
 # paired: 기본값은 FALSE, 대응표본 t검정 수행 시 TRUE로 지정
 # m: 검정의 기준이 되는 값으로, 기본값은 0 / 대응표본 t검정에서는 모평균의 차이가 0인지를 검정하기 때문에 m 인자는 적지 않아도 됨

# 데이터 입력
data <- data.frame(before = c(7,3,4,5,2,1,6,6,5,4),
                   after = c(8,4,5,6,2,3,6,8,6,5))

# 대응표본 t검정 
t.test(data$before, data$after, alternative = "less", paired = TRUE)




# 3. 독립표본 t-검정
# 3-1. t검정 수행 전, 등분산 검정 필요 
# 3-1-1. var.test(x, y, alternative)
 # x: 모집단1로부터 측정한 관측값(수치형 벡터) / y: 모집단2로부터 측정한 관측값(수치형 벡터)
# 3-1-2. var.test(formula, data, alternative)
 # formula: 데이터프레임을 var.test함수에 적용시킬 때 사용 / 수치형 벡터(종속변수)~집단분류(독립변수)

# 3-2. t검정 함수
# 3-2-1. t.test(x, y, alternative, var.equal=FALSE)
# 3-2-2. t.test(formula, data, alternative, var.equal=FALSE)
 # var.equal: 등분산성을 만족하는지의 여부 (TRUE/FALSE)

library(MASS)
data("cats")

# 등분산 검정
var.test(Bwt~Sex, data=cats)

# 등분산성을 만족하지 않는다는 조건 하에 t검정 수행
t.test(Bwt~Sex, data=cats, alternative="two.sided", var.equal=FALSE)
