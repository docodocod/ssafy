T=int(input())
for test_case in range(1,T+1):
    lst=[]
    x,y=0,0
    p,q=map(int,input().split())
    arr=[[0]*301 for _ in range(301)]
    for i in range(1,301):
        arr[i][1]=i+arr[i-1][1]
        if arr[i][1]==q:
            lst.append((i,1))
        if arr[i][1]==p:
            lst.append((i,1))
        for j in range(2,301):
            arr[i][j]=arr[i][j-1]+i+j-2
            if arr[i][j]==q:
            	lst.append((i,j))
            if arr[i][j]==p:
                lst.append((i,j))
    for sx,sy in lst:
        x+=sx
        y+=sy
    print(f'#{test_case} {arr[x][y]}')
        
    #comment:
    #범위를 잘못 잡아서 테케 10개까지 밖에 안됐는데 수정 후 998까지 밖에 success가 안돼서 생각하다가
    #q,p가 만약 값이 같다면? 이라는 제약조건을 생각을 못했다
    #수정 후 다시 푸니 성공

    #문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw

        
                
    