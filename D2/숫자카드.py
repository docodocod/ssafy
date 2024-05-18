T=int(input()) #테스트 케이스 횟수 입력
for test_case in range(1,T+1):
    N=int(input()) # 카드 수 입력
    card=list(map(int,input())) #카드 숫자들 map으로 쪼개서 입력
    cnt=[0]*10 # 카운트 할 리스트 만들기
    for number in card: # cnt에 카드 횟수 담기
        cnt[number]+=1

    idx=0 
    max_cnt=0
    for i in range(len(cnt)): # 카드번호와 최대 횟수 찾기
        if max_cnt<=cnt[i]:
            max_cnt=cnt[i]
            idx=i
    print(f'#{test_case} {idx} {max_cnt}')

    #문제: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
