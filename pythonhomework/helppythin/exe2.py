sum=0
count=0
num=int(input("Enter a number:"))
while num//10==0:
    sum=sum+num
    count=count+1
    num=int(input("Enter a number"))
print(sum/num)


