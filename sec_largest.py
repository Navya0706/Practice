n=int(input())
arr = list(map(int,input().split()))
a=max(arr)
print(a)
for i in arr:
    if i == a:
        arr.remove(a)
b=max(arr)
print(b)