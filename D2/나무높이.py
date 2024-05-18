def grow_water(mx_tree,tree):
    result=0
    for i in range(len(tree)):
        if mx_tree==tree[i]:
            continue
        goal=tree[i]
        day=1
        while True:
            if day%2==1:
                goal+=1
                result+=1
                if goal==mx_tree:
                    break
                elif goal==mx_tree-1:
                    goal-=1
            elif day%2==0:
                goal+=2
                result+=1
                if goal==mx_tree:
                    break
            day+=1
    return result
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    result=0
    tree=list(map(int,input().split()))
    mx=max(tree)
    result=grow_water(mx,tree)
    print(f'#{test_case} {result}')

#comment 
#와 뭐가 틀린거야...