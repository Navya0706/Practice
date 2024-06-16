arr = input()
vowels = ['a','e','i','o','u']
count=0
for i in arr:
    if i in vowels:
        count+=1
print(count)