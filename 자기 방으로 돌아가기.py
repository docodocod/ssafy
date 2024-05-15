T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=[0]*200
    for i in range(N):
        s,e=map(int,input().split())
        if e<s:
            s,e=e,s
        for j in range((s-1)//2,(e-1)//2+1):
            lst[j]+=1
    print(f'#{test_case} {max(lst)}')

#comment
#1부터 400까지 방에서 겹치는 곳이 있으면 1을 하나씩 더해서 구했는데 제약조건 중 시작 방과 끝나는 방이 무조건
#끝나는 방이 시작방보다 크다는건 없었음 그래서 계속 test case 9까지 실패하다가
#문제 보면서 방이 일렬로 나란히 있는것이 아니라 복도를 두고 양쪽으로 있으므로 범위를 조정해줘야 했다.
#쉬운줄 알았는데 결국 답지 봄

# 문제 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8