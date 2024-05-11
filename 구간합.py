T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split()) # 배열 수, 구간 입력 받기
    lst=list(map(int,input().split())) #숫자 list로 입력 받기
    mx=0 # 임시 mx값
    mn=10000000 # 임시 mn값
    for i in range(0,N-M+1):
        sm=0 #sum을 for문 끝날때마다 초기화
        for j in range(i,i+M):
            sm+=lst[j]
        if sm>mx:
            mx=sm
        if sm<mn:
            mn=sm
    print(f'#{test_case} {mx-mn}')

#문제: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
