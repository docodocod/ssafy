#A사는 1리터당 P원의 돈을 지출
#B사는 기본요금 Q원 월간 사용량 R이하인 경우 기본요금 
#but R이상인 경우 초과량에 대해 1리터당 S원 지출
#P=A사 리터당 요금
#Q=B사 기본요금
#R=B사 기본용랑
#R

T=int(input())
for test_case in range(1,T+1):
    P,Q,R,S,W=map(int,input().split())
    over=0
    A=P*W
    if W<=R:
        B=Q
    elif W>R:
        over=(W-R)*S
        B=Q+over
    print(f'#{test_case} {min(A,B)}')

#comment:
#쉬움

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3