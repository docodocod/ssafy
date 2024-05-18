T=10
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    cnt=0
    
    for i in range(2,N-2):
        center=lst[i]
        if lst[i-2]<center and lst[i-1]<center and lst[i+1]<center and lst[i+2]<center:
            mx=max(lst[i-2],lst[i-1],lst[i+2],lst[i+1])
            cnt+=center-mx
    print(f'#{test_case} {cnt}')