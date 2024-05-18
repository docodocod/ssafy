T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    up=down=0
    up_mx=down_mx=0
    for i in range(N-1):
        if lst[i]<lst[i+1]:
            up=lst[i+1]-lst[i]
            if up_mx<up:
                up_mx=up
        elif lst[i]>lst[i+1]:
            down=lst[i]-lst[i+1]
            if down_mx<down:
                down_mx=down
        elif lst[i]==lst[i+1]:
            continue
    print(f'#{test_case} {up_mx} {down_mx}')

#comment:
#쉽지만 페이지에서 파이썬은 지원하지 않음


