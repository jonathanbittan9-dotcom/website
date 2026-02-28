sum=0
num=int(input("Enter a number:"))
while num!=0:
    num2=num%10
    num=num//10
    sum=sum+num2
print("sum of digits:",sum)