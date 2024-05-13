T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt=0
            for si in range(si,si+M):
                for sj in range(sj,sj+M):
                    cnt+=arr[i][j]
        if ans<cnt:
            ans=cnt
    print(f'#{test_case} {ans}')
# comment
# 4중 for문이라 좀 헷갈렸지만 성공