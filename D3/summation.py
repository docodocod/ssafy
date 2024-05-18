T=int(input())
for test_case in range(1,T+1):
    lst=list(map(str,input().split()))
    ans=[]
    for s in lst:
        sm=0
        for number in s:
            sm+=int(number)
        ans.append(sm)
    print(f'#{test_case} {max(ans)} {min(ans)}')