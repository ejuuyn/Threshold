choose_shape=int(input("도형을 선택하세요\n""1. 계단\n""2. 더하기\n""3. 종료\n"))


if choose_shape==1:
    st_height=int(input("계단의 높이를 입력하세요(2이상 5이하)"))
    st_step=int(input("계단의 칸 수를 입력하세요(2이상 5이하)"))
    for i in range(st_step):
        i=1
        if i<=st_step:
            i+=1
        for k in range(i*st_step):
            print("■"*st_height*i,end="")
        print("\n")

if choose_shape==2:
    n=int(input("더하기의 길이를 입력하세요(2이상 10이하):"))
    for i in range(n) :
       for k in range(n) :
          print(" ",end="")
       for k in range(n) :
          print("*",end="")
       print() 
    for i in range (n) :
       for k in range(3*n) :
          print("*", end="")
       print("")

    for i in range(n) :
       for k in range(n) :
          print(" ",end="")
       for k in range(n) :
          print("*",end="")
       print('')
