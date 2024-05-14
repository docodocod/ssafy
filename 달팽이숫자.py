di=[0,1,0,-1] #i 방향
dj=[1,0,-1,0] #j 방향

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)] # 배열 모두 0으로 초기화
    
    i,j,cnt,dr=0,0,1,0 #사용할 변수들 초기화
    arr[i][j] = cnt #첫번째 시작값 초기화
    cnt+=1

    while cnt<=N*N:
        ni,nj=i+di[dr],j+dj[dr] #다음 배열로 이동
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: #범위내에 있고 다음 수가 0이면
            i,j=ni,nj
            arr[i][j]=cnt
            cnt+=1
        else: #그렇지 않으면
            dr=(dr+1)%4 #방향 회전
    
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)