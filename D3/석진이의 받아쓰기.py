T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst1=input()
    lst2=input()
    cnt=0
    for i in range(N):
        if lst1[i]==lst2[i]:
            cnt+=1
    print(f'#{test_case} {cnt}')

#comment:
#사이트에서 디버깅 불가능
#정답은 맞음