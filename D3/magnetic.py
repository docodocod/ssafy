T=10
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)] 
    arr_t=list(zip(*arr))
    ans=0
    for i in range(N):
        pre=0 # 이전값 저장하기 위한 변수 초기화
        for j in range(N):
            if arr_t[i][j]==1: # N극은 1 S극은 2 이므로 만약 N극을 만났다면?
                pre=1 # N극을 저장
            if arr_t[i][j]==2 and pre==1: # 만약 S극을 만나고 직전에 만났던 것이 N극이라면?
                ans+=1 #답에 +1 추가
                pre=0 # N극과 S극이 만났으므로 pre 변수는 0으로 초기화 시켜준다.
    print(f'#{test_case} {ans}')

#comment:
#자석이 위에서 아래로 끌려서 합쳐지는 문제이므로 보기가 힘들어 배열을 역치 시켜서 품

#문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD