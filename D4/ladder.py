T=10
for test_case in range(1,T+1):
    _=input()
    ci=99 #마지막 행
    cj=0 # 목적지 열 초기화
    N=100 # 배열 수 
    arr=[[0]+list(map(int,input().split()))+[0] for _ in range(N)] #범위내 계산하기 위해 [0]을 추가로 삽입
    for j in range(N+2): # 목적지 배열 인덱스 찾기
        if arr[ci][j]==2:
            cj=j
            break
    while ci>0: # 0행까지 계쏙 반복하기
        if arr[ci][cj-1]==1: #왼쪽이 1이면 현재 내 위치 0으로 만들기
            arr[ci][cj]=0
            cj-=1 #왼쪽으로 이동
        elif arr[ci][cj+1]==1: #오른쪽이 1이면 현재 내 위치 0으로 만들기
            arr[ci][cj]=0
            cj+=1 # 오른쪽으로 이동
        else: # 왼쪽과 오른쪽 둘다 1이 없다면
            ci-=1 # 위로 이동
    print(f'#{test_case} {cj-1}') 

#Comment
#dfs로 풀려다가 방법이 기억이 안남 ㅎ
#출발점부터 시작해서 하나씩 다 돌아가면 왠지 시간초과가 날 것 같아 목적지부터 시작하여 출밟점을 찾는 방법을 택

# 문제 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
