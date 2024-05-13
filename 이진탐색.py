def binary_search(page,key):
    start=1 #시작 페이지
    end=page #끝 페이지 
    count=0 #몇번 하나 횟수
    while True:
        middle=(start+end)//2 #먼저 책을 펼쳐준다
        count+=1 #횟수 추가
        if middle==key: #키값과 맞으면 횟수 반환
            return count
        elif middle>key: #키값보다 크면 end값 초기화
            end=middle
        elif middle<key: #키값보다 작으면 start 초기화
            start=middle

T=int(input())
for test_case in range(1,T+1):
    page,A,B=map(int,input().split())
    answer1=binary_search(page,A)
    answer2=binary_search(page,B)
    if answer1>answer2:
        print(f'#{test_case} B')
    elif answer2>answer1:
        print(f'#{test_case} A')
    elif answer1==answer2:
        print(f'#{test_case} 0')
