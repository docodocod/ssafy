T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[[0]*10 for _ in range(10)] # 10x10 배열 선언 후 0으로 초기화
    answer=0 #정답 초기화
    for _ in range(N):
        s_x,s_y,e_x,e_y,cnt=map(int,input().split()) # x,y값 각각 받기
        for i in range(s_x,e_x+1):
            for j in range(s_y,e_y+1):
                arr[i][j]+=cnt #컬러 숫자 하나씩 넣어주기
    for a in arr:
        for number in a:
            if number>=3: #색깔이 여러개 겹칠 경우 3이상의 숫자이므로
                answer+=1 #색깔이 겹칠 경우 +1
    print(f'#{test_case} {answer}')

# comment 
# 아직까지는 쉽다.

#문제: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
