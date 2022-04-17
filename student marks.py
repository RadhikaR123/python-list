s = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']

m = [10, 20, 56, 45, 36, 20]
student_marks=[]

print (len(s))

print (len(m))
sum=0

i=0
while i<len(s):
    sum=s[i]+ str(m[i])
    student_marks.append(sum)
    i=i+1
print(student_marks)
