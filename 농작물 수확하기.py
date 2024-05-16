T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    sum=0
    for i in range(N):
        if i<=N//2:
            for j in range((N//2)-i,(N//2)+i+1):
                sum+=arr[i][j]
        elif i>N//2:
            for j in range(i-(N//2),N+(N//2)-i):
                sum+=arr[i][j]
    print(f'#{test_case} {sum}')
    
    #comment
    #범위 구하는데 시간을 좀 소비함