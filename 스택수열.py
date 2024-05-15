N=int(input())
stack,ans,find=[],[],True
count=0
j=0
arr=[]
for i in range(N):
    stack[i]=int(input())
while len(lst)>j:
    if number[-1]==lst[j]:
        a=number.pop()
        arr.append(a)
        ans.append("-")
        j+=1
    elif number[-1]!=lst[j]:
        count+=1
        number.append(count)
        ans.append("+")
if lst==arr:
    for i in ans:
        print(i)
else:
    print('NO')


    