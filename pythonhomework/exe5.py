sum=0
count=1
grade=int(input("Enter a grade:"))
while (grade>=0 and grade<=100):
    sum=sum+grade
    count=count+1
    grade=int(input("Enter a grade:"))
avg=sum/count
print("The average is:",avg)