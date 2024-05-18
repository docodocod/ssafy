T=int(input())
for test_case in range(1,T+1):
    N=input()
    visited=[0]*10
    cnt=0
    for number in N:
        if visited[int(number)]!=1:
            visited[int(number)]=1
            cnt+=1
        elif visited[int(number)]==1:
            continue
    print(f'#{test_case} {cnt}')

# comment:
# 웹에서 파이썬을 지원하지 않는 문제임...
# 일단 테케는 성공