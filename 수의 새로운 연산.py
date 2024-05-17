T=int(input())
for test_case in range(1,T+1):
    lst=[]
    x,y=0,0
    p,q=map(int,input().split())
    arr=[[0]*201 for _ in range(201)]
    for i in range(1,201):
        arr[i][1]=i+arr[i-1][1]
        if arr[i][1]==q or arr[i][1]==p:
            lst.append((i,1))
        for j in range(2,201):
            arr[i][j]=arr[i][j-1]+i+j-2
            if arr[i][j]==q or arr[i][j]==p:
                lst.append((i,j))
    for sx,sy in lst:
        x+=sx
        y+=sy
    print(f'#{test_case} {arr[x][y]}')

    #comment:
    #테케 10개까지는 풀었지만 over flow로 인해 런타임 에러가 생겼다 나중에 다시풀기...
    
        
                
    