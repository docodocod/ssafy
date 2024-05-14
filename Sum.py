T=10
for test_case in range(1,T+1):
    _=input()
    N=100
    arr=[list(map(int,input().split())) for _ in range(N)] # 100x100 배열 받기
    left_diag,right_diag=0,0,0,0 # 행,열,대각의 합들을 저장할 변수 초기화
    mx=0 #max값 초기화
    for i in range(N):
        row,cul=0,0 # 행 / 열이 바뀔 때마다 초기화 해줘야함
        for j in range(N): 
            row+=arr[i][j] #행 합산
            cul+=arr[j][i] #열 합산
        mx=max(row,cul,mx)
        right_diag+=arr[i][i] # 대각선은 한줄 밖에 없으므로 첫번째 for문에다가 두면 된다.
        left_diag+=arr[i][N-i-1]
    print(f'#{test_case} {max(mx,right_diag,left_diag)}')
    # comment
    # 이번 문제는 쉽게 넘어갔다.


    # 문제 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh



            