input_list=input("Enter the numbers separated by spaces:")
numbers=list(map(int,input_list.split()))
print(input_list)

count=numbers.count(input_list)
print(count)

numbers.insert(4,11)
print(numbers)

numbers.append(7)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.copy()
print(numbers)

numbers.clear()
print(numbers)

numbers.extend([8,9,10])
print(numbers)

numbers.pop(2)
print(numbers)

numbers.reverse()
print(numbers)
