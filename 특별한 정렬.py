T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    result=[0]*10
    i=0
    j=1
    lst.sort()
    for row in lst:
        if j>=10:
            break
        result[j]=row
        j+=2
    lst.reverse()
    for high in lst:
        if i>=10:
            break
        result[i]=high
        i+=2
    print(f'#{test_case}',*result)

    #comment: 뭔가 더 깔끔하게 할 수 있을 것 같은데....

    # 문제: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do