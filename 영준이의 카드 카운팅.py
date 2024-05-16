dct={'S':0,'D':1,'H':2,'C':3}

T=int(input())
for test_case in range(1,T+1):
    st=input()
    arr=[[] for _ in range(4)]
    ans=[]
    for i in range(0,len(st),3):
        arr[dct[st[i]]].append(int(st[i+1:i+3]))
    
    for j in range(4):
        if len(arr[j])!=len(set(arr[j])):
            print(f'#{test_case} ERROR')
            break
        else:
            ans.append(13-len(arr[j]))
    print(f'#{test_case}',*ans)

        