T=10
for test_case in range(1,T+1):
    _=input()
    arr=[[0]+list(map(int,input().split()))+[0] for _ in range(100)]
    arr_v=arr
    cnt,mx=0,0
    ci,cj=0,0
    for sj in range(1,101):
        cj=sj
        while ci<100:
            arr_v[ci][cj]=0
            cnt+=1
            if arr[ci][cj-1]==1:
                cj-=1
            elif arr[ci][cj+1]==1:
                cj+=1
            else:
                ci+=1
        if mx<cnt:
            mx=cnt
            idx=cj
        arr_v=arr
    print(f'#{test_case} {idx}')

    #comment
    #아직 못품

    # 문제 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh&categoryId=AV14BgD6AEECFAYh&categoryType=CODE&problemTitle=ladder&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

        