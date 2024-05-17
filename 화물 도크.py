T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    time_table=[0]*25
    ans=0
    lst=[list(map(int,input().split())) for _ in range(N)]
    
    for s,e in lst:
        if s>12= or
        for i in range(s,e+1):
            time_table[i]+=1
        if time_table[i]>=2:
            break
        ans+=1 
    print(f'#{test_case} {ans}')


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1])

    ans=last=0

    for s,e in arr:
        if last<=s:
            ans+=1
            last=e
    print(f'#{test_case} {ans}')

    #comment:
    #시간이 좀 걸려서 답지를 봤는데 lambda 문법을 잘 모른다... 공부해야겠다.
    
    #문제: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXxOiEN6SU0DFASZ