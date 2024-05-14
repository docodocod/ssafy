T=10
for test_case in range(1,T+1):
    _=input()
    ci=99
    cj=0
    N=100
    arr=[[0]+list(map(int,input().split()))+[0] for _ in range(N)]
    for j in range(N+2):
        if arr[ci][j]==2:
            cj=j
            break
    while ci>0:
        if arr[ci][cj-1]==1:
            arr[ci][cj]=0
            cj-=1
        elif arr[ci][cj+1]==1:
            arr[ci][cj]=0
            cj+=1
        else:
            ci-=1
    print(f'#{test_case} {cj-1}')

#Comment
#dfs로 풀려다가 방법이 기억이 안남 ㅎ

# 문제 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
