numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
length=len(numbers)
a=max(numbers)
numbers.remove(a)
#print(numbers)
sec_max=numbers[0]
i=0
while i<length-1:
    if numbers[i]>sec_max:
        sec_max=numbers[i]
    i=i+1
print("second maximum number is :", sec_max)
