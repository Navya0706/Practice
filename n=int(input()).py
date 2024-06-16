n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
    if(sum(arr[:i+1])==0):
        count=count+1
print(count)