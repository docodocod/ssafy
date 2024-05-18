def change(arr):
    arr_change=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_change[i][j]=arr[N-j-1][i]
    return arr_change

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    
    arr_90=change(arr)
    arr_180=change(arr_90)
    arr_270=change(arr_180)
    print(f'#{test_case}')
    for a,b,c in zip(arr_90,arr_180,arr_270):
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')

#comment:
#문제는 다 풀었지만 옆으로 출력하는걸 몰라서 답지 봄...