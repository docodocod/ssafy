T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    sm=0
    for i in range(N):
        mx=lst.index(max(lst))
        if i==mx:
            lst[i]=0
        else:
            sm+=lst[mx]-lst[i]
            lst[i]=0
    print(f'#{test_case} {sm}')
#comment
#테케 7까지 되고 그 이후 시간초과가 나온다...