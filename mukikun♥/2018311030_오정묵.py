def make_stair():
    st_height=int(input("계단의 높이를 입력하세요(2이상 5이하):"))
    while st_height<2 or st_height>5 :
        st_height=int(input("입력이 잘못되었습니다. 다시 입력해주세요.(2이상 5이하):"))
    st_step=int(input("계단의 칸 수를 입력하세요(2이상 5이하):"))
    while st_step<2 or st_step>5 :
        st_step=int(input("입력이 잘못되었습니다. 다시 입력해주세요.(2이상 5이하):"))
    for i in range (st_step) :
           for j in range (st_height) :
               print("■■■"*(i+1))

def make_plus():
    plus_size=int(input("더하기의 길이를 입력하세요(2이상 10이하):"))
    while plus_size<2 or plus_size>10 :
        plus_size=int(input("입력이 잘못되었습니다. 다시 입력해주세요.(2이상 10이하):"))
    for i in range(plus_size):
         print(" "*plus_size,end="")
         print("*"*plus_size)
    for j in range(plus_size):
         print("*"*3*plus_size)
    for k in range(plus_size):
         print(" "*plus_size,end="")
         print("*"*plus_size)

while(True):
    choose_shape=int(input("도형을 선택하세요\n""1. 계단\n""2. 더하기\n""3. 종료\n"))
    if choose_shape==1:
        make_stair()

    elif choose_shape==2:
        make_plus()

    elif choose_shape==3:
        break
    
    else:
        print("입력이 잘못되었습니다.")
