T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    K=1
    lst=[0]*10
    while len(set(lst))<10:
        N=N*K
        for number in str(N):
            lst[int(number)]=number
        K+=1
    print(f'#{test_case} {K}')