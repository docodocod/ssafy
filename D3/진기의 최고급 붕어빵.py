T=int(input())
for test_case in range(1,T+1):
    N,M,K=map(int,input().split())
    a,b=map(int,input().split())
    if a<b:
        a,b=b,a
    if 