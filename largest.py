n = int(input())
arr = list(map(int, input().split()))
largest=0
sec_largest=0
if n>=2 or n<=10:
        for i in arr:
            if arr[i]>=-100 or arr[i]<=100:
                arr[1]=largest
            if arr[i]>largest:
                largest=arr[i]
arr[1]=sec_largest
if arr[i]>sec_largest and arr[i]==largest:
    sec_largest=arr[i]
print(sec_largest)
                