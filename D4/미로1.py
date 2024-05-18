def bfs(si,sj):
    q=[]
    v=[[0]*N for _ in range(N)]
    v[si][sj]=1
    q.append((si,sj))
    while q:
        ci,cj=q.pop(0)
        if arr[ci][cj]==3:
            return 1
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1 and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
    return 0

T=int(input())
for test_case in range(1,T+1):
    N=16
    si,sj=1,1
    arr=[list(map(int,input())) for _ in range(N)]
    ans=bfs(si,sj)
    print(f'#{test_case} {ans}')

#comment:
#처음에는 visit배열을 굳이 만들어야 할까?라는 생각을 했는데 for문 돌 때 생각을 잘못했다.
#visit배열을 만들지 않고 했더니 무한루프 돌았다.
