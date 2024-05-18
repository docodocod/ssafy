def bfs(si,sj):
    q=[] #q배열 선언
    v=[[0]*N for _ in range(N)] #visited 배열 선언
    q.append((si,sj)) #스타트 좌표 q에 추가
    v[si][sj]=1 #스타트 배열 1선언
    while q:
        ci,cj=q.pop(0)
        if arr[cj][cj]==3:
            return v[ci][cj]-2

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return 0
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                si,sj=i,j #start 좌표 찾기
    ans=bfs(si,sj)
    print(f'#{test_case} {ans}')
