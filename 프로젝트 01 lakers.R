# 01.00 소스 불러오기 ----
source("D:/googledrive/Activation/Business/Lecture/2021 패스트캠퍼스/초격차/Fastcampus/PT-VOD/05 데이터 집계와 변환/source_test.R")

# usethis::edit_file("D:/googledrive/Activation/Business/Lecture/2021 패스트캠퍼스/초격차/Fastcampus/PT-VOD/05 데이터 집계와 변환/source_test.R")

# 01.10 데이터 불러오기 ----
data()

lakers <- lubridate::lakers %>% 
  as_tibble()


# 01.20 데이터 현황 확인하기 ----
lakers %>% 
  colnames %>% 
  as_tibble() %>% 
  write_clip()
 
lakers %>% 
  tail(10) %>% 
  t


# 02.00 전처리 ----

# 02.10 NA 및 결측치 현황 파악 ----


lakers %>% 
  count(date) %>% 
  print(n=100)

lakers %>% 
  count(opponent) %>% 
  print(n=100)

lakers %>% 
  count(game_type) %>% 
  print(n=100)

lakers %>% 
  count(time, period) %>% 
  data.table %>% 
  dcast.data.table(time ~ period, value.var = "n", sum) %>% 
  as_tibble() %>% 
  print(n=1000)

lakers %>% 
  count(time) %>% 
  print(n=10000)

lakers %>% 
  count(period) %>% 
  print(n=100)

lakers %>% 
  count(etype) %>% 
  print(n=10000)

lakers %>% 
  count(team) %>% 
  print(n=10000)


lakers %>% 
  filter(date == '20081028') %>% 
  print(n=10000)

# 02.11 결측치 : player ----
lakers %>% 
  count(player) %>% 
  print(n=10000)

# 02.12 결측치 : result ----
lakers %>% 
  count(result)

lakers %>% 
  filter(player %>% nchar() <1)

lakers %>% 
  count(points)

# 02.13 결측치 : type ----
lakers %>% 
  count(type) %>% 
  print(n=100)

# 02.14 결측치 : x,y ----
lakers %>% 
  count(x,y) %>% 
  tail


# 02.20 NA 및 결측치 처리 ----
lakers <- lakers %>% 
  mutate(player = ifelse(player %>% nchar() < 1, NA, player),
         result = ifelse(result %>% nchar() < 1, NA, result),
         type = ifelse(type %>% nchar() < 1, NA, type))

# 02.30 date 형태 변환 ----
lakers <- lakers %>% 
  mutate(date = date %>% ymd)

# 02.31 행동 유형을 긍/부정으로 나누어보자. ----
lakers <- lakers %>% 
  mutate(etype =   ifelse(etype == "free throw", 'free_throw', etype),
         etype_2 = ifelse(etype %in% c("ejection","foul","timeout","turnover","violation"),"neg",
                   ifelse(etype %in% c("jump ball","sub"),"neu",'pos')),
         etype_3 = ifelse(etype == 'ejection',-3,
                   ifelse(etype %in% c('violation','foul'),-2,
                   ifelse(etype %in% c('turnover','timeout'),-1,
                   ifelse(etype %in% c('sub','jump ball'),0,
                   ifelse(etype == 'rebound',1,
                   ifelse(etype == 'shot',2,3)))))))



# 03.32 이적 등 여러가지 이유로 경기당 기준으로 계산해보자 ----
key_player_spec <- lakers %>% 
  filter(!player %>% is.na) %>% 
  group_by(team, date, player, etype) %>% 
  summarise(ability = sum(etype_3)) %>% 
  group_by(team, player, etype) %>% 
  summarise(avg_ability = mean(ability)) %>% 
  data.table() %>% 
  dcast(team + player ~ etype, value.var = "avg_ability",  sum) %>% 
  as_tibble() 

key_player_sum <- lakers %>% 
  filter(!player %>% is.na) %>% 
  group_by(team, date, player, etype) %>% 
  summarise(ability = sum(etype_3)) %>% 
  group_by(team, player, etype) %>% 
  summarise(avg_ability = mean(ability)) %>% 
  group_by(player) %>% 
  summarise(sum_ability = sum(avg_ability))

key_player <- left_join(key_player_spec,key_player_sum)

key_player %>% 
  filter(team == "LAL") %>% 
  arrange(sum_ability %>% desc) %>% 
  write_clip()


# 03.13 팀별 평균 역량은 어떠한가?
team_score <- key_player %>% 
  group_by(team) %>% 
  summarise(avg_ability = mean(sum_ability),
            min_ability = min(sum_ability),
            max_ability = max(sum_ability),
            sd_ability = sd(sum_ability)) %>% 
  arrange(avg_ability %>% desc)


key_player %>% 
  arrange(team, sum_ability %>% desc) %>% 
  # filter(team %in% c('ATL', "LAL", 'BOS')) %>% 
  distinct(team,.keep_all = T) %>% 
  arrange(sum_ability %>% desc) %>% 
  distinct(player, .keep_all = T) %>% 
  print(n= 100)


# 03.20 경기가 열세한 상황에서 선수들은 평소와 어떤 차이를 보이는가?

# 03.21 특정 경기의 승패는 어떠한가?
lakers %>% 
  filter(date == '2008-10-28') %>% 
  group_by(team) %>% 
  summarise(points = sum(points)) %>% 
  filter(team != "OFF")

# 03.22 특정 경기내 각 쿼터별 승패는 어떠한가?
lakers %>% 
  filter(date == '2008-10-28') %>% 
  group_by(team, period) %>% 
  summarise(points = sum(points)) %>% 
  filter(team != "OFF") %>% 
  data.table() %>% 
  dcast.data.table(period ~ team, value.var = "points") %>% 
  as_tibble()

# 03.23 특정 경기에서 각 쿼터 내 분별 점수는 어떠한가?
# > 분별로 보기엔 너무 범위가 촘촘하다. 그러므로 쿼터별로 기준을 고려한다.
lakers %>% 
  mutate(min = time %>% str_sub(1,2)) %>% 
  filter(date == '2008-10-28') %>% 
  group_by(team, period, min) %>% 
  summarise(points = sum(points)) %>% 
  filter(team != "OFF") %>% 
  data.table() %>% 
  dcast.data.table(period + min ~ team, value.var = "points") %>% 
  as_tibble()

# 03.24 특정 경기 내 각 쿼터별 열세 우세를 나누자.
lakers %>%
  filter(date == '2008-10-28') %>% 
  group_by(date, team, period) %>% 
  summarise(points = sum(points)) %>% 
  filter(team != "OFF") %>% 
  mutate(tag_order = ifelse(team == "LAL",1,2)) %>% 
  arrange(date, period, tag_order) %>% 
  group_by(period) %>% 
  mutate(opp_points = lead(points)) %>% 
  filter(tag_order == 1) %>% 
  group_by(date) %>% 
  summarise(cum_points = cumsum(points),
            cum_opp_points = cumsum(opp_points)) %>% 
  mutate(points_gap = cum_points - cum_opp_points,
         points_yn = ifelse(points_gap > 0, '1',
                            ifelse(points_gap == 0,'0',
                                   ifelse(points_gap < 0, '-1','error'))),
         points_yn = points_yn %>% as.numeric,
         period = paste0("p_",row_number()))

# 03.25 전체 경기로 배분해보자.
play_result <- lakers %>% 
  group_by(date, team, period) %>% 
  summarise(points = sum(points)) %>% 
  filter(team != "OFF") %>% 
  mutate(tag_order = ifelse(team == "LAL",1,2)) %>% 
  arrange(date, period, tag_order) %>% 
  group_by(period) %>% 
  mutate(opp_points = lead(points)) %>% 
  filter(tag_order == 1) %>% 
  group_by(date) %>% 
  summarise(cum_points = cumsum(points),
            cum_opp_points = cumsum(opp_points)) %>% 
  mutate(points_gap = cum_points - cum_opp_points,
         points_yn = ifelse(points_gap > 0, '1',
                     ifelse(points_gap == 0,'0',
                     ifelse(points_gap < 0, '-1','error'))),
         points_yn = points_yn %>% as.numeric,
         period = paste0("p_",row_number()))%>% 
  data.table() %>% 
  dcast.data.table(date ~ period, value.var = "points_yn", fill = 0) %>% 
  as_tibble() %>% 
  mutate(play_result = p_1 + p_2 + p_3 + p_4 + p_5)




# 03.26 일반적인 상황일 때 Lakers 선수들은 평소 어떤 행동을 보이는가? ----
play_status_type_2 <-  lakers %>% 
  filter(team == "LAL") %>% 
  group_by(date, etype_2) %>% 
  summarise(etype_3 = sum(etype_3)) %>% 
  data.table() %>% 
  dcast.data.table(date ~ etype_2, value.var = "etype_3", sum) %>% 
  as_tibble()


play_status_type_2_result <- left_join(play_status_type_2, play_result) %>% 
  mutate(result_grp = ifelse(play_result > 0, 'result_pos',
                      ifelse(play_result == 0,'result_neu',
                      ifelse(play_result < 0, 'result_neg','error')))) %>% 
  arrange(play_result) %>% 
  group_by(result_grp) %>% 
  summarise(avg_neg = mean(neg),
            avg_pos = mean(pos),
            avg_neu = mean(neu))




play_status_type_1 <-  lakers %>% 
  filter(team == "LAL") %>% 
  group_by(date, etype_2, etype) %>% 
  summarise(etype_3 = sum(etype_3))

play_status_type_1_result <- left_join(play_status_type_1, play_result) %>% 
  mutate(result_grp = ifelse(play_result > 0, 'result_pos',
                      ifelse(play_result == 0,'result_neu',
                      ifelse(play_result < 0, 'result_neg','error')))) %>% 
  arrange(play_result) %>% 
  group_by(result_grp, etype, etype_2) %>% 
  summarise(etype_3 = mean(etype_3)) %>% 
  data.table() %>% 
  dcast.data.table(etype_2 + etype ~ result_grp, value.var = "etype_3", sum) %>% 
  as_tibble()



play_status_overview_result <- left_join(play_status_type_1, play_result) %>% 
  mutate(result_grp = ifelse(play_result > 0, 'result_pos',
                      ifelse(play_result == 0,'result_neu',
                      ifelse(play_result < 0, 'result_neg','error')))) %>% 
  arrange(play_result) %>% 
  group_by(etype_2, etype) %>% 
  summarise(result_overview = mean(etype_3))


result_table <- left_join(play_status_type_1_result, play_status_overview_result)




# 03.30 경기별 행동 유형의 추이는 어떠한가?
left_join(play_status_type_2,play_result) %>% 
  mutate(result_yn = ifelse(play_result > 0, "승리",
                     ifelse(play_result == 0, "동점",
                     ifelse(play_result < 0, "패배",99)))) %>% 
  # filter(!result_yn == '동점') %>% 
  mutate(etype_result = neg + pos + neu) %>% 
  group_by(result_yn) %>% 
  e_chart(date) %>% 
  e_line(etype_result, smooth = T) %>% 
  e_color( color = c("skyblue","Red")) %>% 
  e_theme("dark-fresh-cut") %>% 
  e_tooltip(trigger = "axis")



# 03.31 상위 키플레이어별 월별 경기력은 어떠한가?
lakers %>% 
  filter(team == "LAL") %>% 
  mutate(month = date %>% substr(1,7)) %>% 
  group_by(month, player) %>% 
  summarise(etype_3 = sum(etype_3)) %>% 
  inner_join(key_player %>% 
               filter(team == "LAL") %>% 
               arrange(sum_ability %>% desc) %>% 
               head(5) %>% 
               select(player)) %>% 
  group_by(player) %>% 
  e_chart(month) %>% 
  e_line(etype_3, smooth = T) %>% 
  e_tooltip(trigger = "axis")

