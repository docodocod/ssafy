T=10
for test_case in range(1,T+1):
    _=int(input())
    ladder=[[0]+list(map(int,input().split()))+[0] for _ in range(100)]
    mn=100*100
    for sj in range(1,101):
        ladder_v=ladder
        cj=sj
        ci,cnt=0,0
        if ladder[0][sj]==1:
            while ci<100:
                ladder_v[ci][cj]=0
                cnt+=1
                if ladder_v[ci][cj-1]==1:
                    cj-=1
                elif ladder_v[ci][cj+1]==1:
                    cj+=1
                else:
                    ci+=1
            if mn>cnt:
                mn=cnt
                idx=sj-1
    print(f'#{test_case} {idx}')
            