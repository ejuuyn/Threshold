{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81c6a318-2944-4c6d-a081-fddc1cccde79",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1018 체스판 다시그리기\n",
    "n, m = map(int,input().split())  #정수 받기: 원래 판의 배열\n",
    "first_board =[]                  #원래 판을 리스트로 \n",
    "edited_board = []                #수정된 판을 리스트로\n",
    "\n",
    "for _ in range(n):\n",
    "    first_board.append(input())   #n(행)의 개수만큼 원래의 판을 입력(리스트로)\n",
    "    \n",
    "for a in range(n-7):         #전체 체스판에서 시작점을 잡기위함.\n",
    "    for b in range(m-7):     #(-7)을 통해 8*8판의 시작점의 위치를 확인   \n",
    "        index1 = 0           #index1 <- W로 시작할 경우 바뀐 체스판    \n",
    "        index2 = 0           #index2 <- B로 시작할 경우의 체스판\n",
    "        for i in range(a, a+8):\n",
    "            for j in range(b,b+8):   #a,b모두 열의 시작점을 기준으로 +8\n",
    "                if (i+j)%2 == 0:     #행+열이 짝수 -> 시작점의 색과 같은 색\n",
    "                    if first_board[i][j] != 'W':  #W가 아닐때 #!= 같지않다.\n",
    "                        index1 += 1   #왜 index1을 'W'로 시작하는 체스판으로 설정해놓고 'W'가 아닐때 1을 더해줄까?\n",
    "                    if first_board[i][j] != 'B':\n",
    "                        index2 += 1\n",
    "                else:                #행번호+열번호 != 짞수\n",
    "                    if first_board[i][j] != 'B':\n",
    "                        index1 += 1\n",
    "                    if first_board[i][j] != 'W':\n",
    "                        index2 += 1\n",
    "        edited_board.append(min(index1,index2))  #바뀐 체스판의 수 중 작은수를 edited_board 리스트에 추가\n",
    "\n",
    "print(min(edited_board))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d269e4e-d4b2-4682-acb4-8ed89c5feb20",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1085 직사각형 탈출\n",
    "x,y,w,h = map(int,input().split())\n",
    "print(min(x,y,w-x,h-y))         #경계면 까지 가장 가까운 거리 구하기."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca1e7dc2-79ee-4a5c-8cbc-88b273032ddf",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1181 단어정렬  \n",
    "#sort는 문자열도 정렬해준다. 권정열아님.\n",
    "#input()은 겁나 느리다. 아하.!\n",
    "\n",
    "n = int(input())\n",
    "list1=[]\n",
    "\n",
    "for i in range(n):\n",
    "    list1.append(input()) #솔직히 append 뭔지 아직 1도 모르겠음 ㅋㅋ\n",
    "    \n",
    "set_list1=set(list1) ##set으로 변환해서 중복값을 제거 ## set이 뭔데..?\n",
    "list1= list(set_list1)\n",
    "\n",
    "list1.sort()   ## 괄호안에 아무 값도 넣지 않으면 알파벳 순서대로 ㄷ정렬을 해준다.!!\n",
    "list1.sort(key = len) ##sort key는 len 순서대로!.\n",
    "\n",
    "for i in list1:\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7eb36fe-52e0-4013-8390-66aa7b2be35c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1259 펠린드롬수\n",
    "\n",
    "while True:          #while True 왜?\n",
    "    n = input()\n",
    "    \n",
    "    if n == '0':    #0 못오기로 약속~\n",
    "        break\n",
    "        \n",
    "    if n==n[::-1]:   #[::-1]로 반전\n",
    "        print('yes')\n",
    "    else:\n",
    "        print('no')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "09d0ad1d-36a9-4dc6-b4ac-d2e82c3ae4c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 55\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27666\n"
     ]
    }
   ],
   "source": [
    "#백준 1436 영화감독 숌\n",
    "\n",
    "n = int(input())\n",
    "count = 0\n",
    "six_n =666\n",
    " \n",
    "while True :\n",
    "    if '666' in str(six_n):\n",
    "        count += 1\n",
    "    if count == n:\n",
    "        print(six_n)\n",
    "        break\n",
    "    six_n += 1\n",
    "\n",
    "# 사실 뭔지 모르겠습니다. ..\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "299fcac6-8731-49d3-8f32-139bf3dcb61f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1654 랜선 자르기\n",
    "#솔직히 반에 반에 반도 이해가 안됨..모르는 함수도 많고.. 시간 내서 공부 더 할게.\n",
    "import sys #이게 뭐죠?\n",
    "\n",
    "L , N = map(int,input().split())  #랜선의 길이를 담은 리스트\n",
    "lan= [int(input()) for i in range(L)]  #갖고 있는 랜선 중 최대값\n",
    "max_lan = max(lan) #후보군을 담을 리스트\n",
    "res =[]\n",
    "\n",
    "def binary(k,start, end):   #이분 탐색 시작\n",
    "    \n",
    "    while start <= end: #적절한 랜선의 길이를 찾는 알고리즘\n",
    "        mid = (start+end)//2 #중간 위치\n",
    "        lines = 0 #랜선 수\n",
    "        for i in lan :    #구해진 값으로 랜선을 잘라보기 \n",
    "            lines += i // mid # 분할된 랜선 수 \n",
    "        #자른 랜선들이 N보다 작으면 조금 더 작게 잘라야 함\n",
    "        \n",
    "        if lines < N: #랜선의 개수가 분기점\n",
    "            end = mid -1   #조건을 만족하는 경우\n",
    "        else:              #후보군에 넣고 좀 더 크게 만들어보기\n",
    "            res.append(mid)\n",
    "            start = mid +1\n",
    "        \n",
    "binary(N,1,max_lan)  #이분탐색 함수 호출\n",
    "\n",
    "print(max(res))  #후보군에서 최대값 출력\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a677efd5-6099-48bb-8d88-97a90b62362b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 8\n",
      " 5\n",
      " 2\n",
      " 4\n",
      " 1\n",
      " 2\n",
      " 5\n",
      " 7\n",
      " 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NO\n"
     ]
    }
   ],
   "source": [
    "##### 백준 1874 스택수열 #이건 문제 자체가 이해가 안됨..\n",
    "#일단 작성만 합니다. 배껴서\n",
    "\n",
    "n = int(input())\n",
    "s=[]\n",
    "op=[]\n",
    "count =1 \n",
    "temp =True\n",
    "for i in range(n):\n",
    "    num = int(input())\n",
    "    while count <= num:\n",
    "        s.append(count)\n",
    "        op.append('+')\n",
    "        count += 1\n",
    "    if s[-1] == num:\n",
    "        s.pop()\n",
    "        op.append('-')\n",
    "    else:\n",
    "        temp = False\n",
    "if temp == False:\n",
    "    print('NO')\n",
    "else:\n",
    "    for i in op:\n",
    "        print(i)\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bd892960-5eb0-4452-aef0-28a92ff6389f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1920 수찾기 (1).이분탐색\n",
    "# 문제 설명 \n",
    "# N개의 정수가 들어있는 집합 A\n",
    "# M개의 정수가 들어있는 집합 B\n",
    "# 집합 B의 요소들이 집합 A에 포함되어있는지 확인하기\n",
    "\n",
    "from  sys import stdin,stdout\n",
    "n=stdin.readline()\n",
    "N=sorted(map(int,stdin.readline().split()))\n",
    "m=stdin.readline()\n",
    "M=map(int,stdin.readline().split())\n",
    "\n",
    "def binary(l,N, start, end):\n",
    "    if start > end:\n",
    "        return 0\n",
    "    m = (start+end)//2\n",
    "    if l == N[m]:\n",
    "        return 1\n",
    "    elif l<N[m]:\n",
    "        return binary(l,N,start,m-1)\n",
    "    else:\n",
    "        return binary(l,N,m+1,end)\n",
    "    \n",
    "for l in M:\n",
    "    start = 0\n",
    "    end = len(N)-1\n",
    "    print (binary(l,N,start,end))\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7a4aea17-f20b-4263-8544-f8916f0dc700",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1920 수찾기 (2).집합자료형을 통한 포함여부 확인\n",
    "# 문제 설명 \n",
    "# N개의 정수가 들어있는 집합 A\n",
    "# M개의 정수가 들어있는 집합 B\n",
    "# 집합 B의 요소들이 집합 A에 포함되어있는지 확인하기\n",
    "\n",
    "from sys import stdin, stdout\n",
    "n= stdin.readline()\n",
    "N= set(stdin.readline().split())\n",
    "m=stdin.readline()\n",
    "M= stdin.readline().split()\n",
    "\n",
    "for l in M :\n",
    "    stdout.write('1\\n') if l in N else stdout.write('0\\n')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cd7133a-306b-4c90-bbb5-e3c74f8f6757",
   "metadata": {},
   "outputs": [],
   "source": [
    "#백준 1929 소수 구하기 \n",
    "M,N = map(int,input().split())\n",
    "\n",
    "\n",
    "for i in range(M,N+1):\n",
    "    if i == 1:   #1은 소수가 아니기 때에\n",
    "        continue\n",
    "    for j in range(2, int(i** 0.5)+1 ): \n",
    "        if i%j == 0:\n",
    "            break\n",
    "    else:\n",
    "        print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aaae848a-e02b-4b3e-848f-f74551dc02e2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
