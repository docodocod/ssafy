T=int(input())
for test_case in range(1,T+1):
    lst1=list(input())
    lst2=['0']*len(lst1)
    cnt=0
    for i in range(len(lst2)):
        if lst2[i]!=lst1[i]:
            lst2[i:]=lst1[i]*len(lst1[i:])
            cnt+=1
    print(f'#{test_case} {cnt}')

#comment:
#슬라이딩이 아직 좀 부족한 것 같다.

#문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3
