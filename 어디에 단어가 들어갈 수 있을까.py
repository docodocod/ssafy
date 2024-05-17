def count_char(arr): #함수로 만드는게 깔끔
    ans=0 # 답 초기화
    for i in range(N):
        cnt=0 #cnt 0으로 초기화
        for j in range(N):
            if arr[i][j]==0: #만약 0을 만나면 이전까지 cnt 횟수 확인
                if cnt==K: #만약 찾을 글자수가 맞다면 
                    ans+=1 #답에 +1 저장
                cnt=0 # cnt 0으로 초기화
                continue
            elif arr[i][j]==1: #만약 1이면
                cnt+=1 #cnt +1 계속 해주기
        if cnt==K:
            ans+=1
    return ans

T=int(input())
for test_case in range(1,T+1):
    N,K=map(int,input().split()) #배열 크기와 찾을 글자수 입력
    arr=[list(map(int,input().split())) for _ in range(N)]
    arr_t=list(zip(*arr)) #세로도 찾아야 하므로 역치 시켜줌
    ans=count_char(arr)+count_char(arr_t) 
    print(f'#{test_case} {ans}')

#comment:
#뭔가 깔끔하지는 않은것 같은데 어쩄든 성공