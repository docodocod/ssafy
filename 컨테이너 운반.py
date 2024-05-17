T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))

    lst1.sort(reverse=True)
    lst2.sort(reverse=True)

    ans=i=0
    for n in lst1:
        if n<=lst2[i]:
            ans+=n
            i+=1
            if i==M:
                break
    print(f'#{test_case} {ans}')
    
    #comment:
    #계속 런타임 오류가 나서 답안지 봤는데 너무 복잡하게 풀었다.

    #문제: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do