sum=0
count=0
num=int(input("Enter a number:"))
while num//10==0 or num//10==-1:
    sum=sum+num
    count=count+1
    num=int(input("Enter a number:"))
if count==0:
    print(0)
else:
    avg=sum/count
    print(avg)


# Input: 5 7 3 10
# Output: 5

# Input: -2 -4 12
# Output: -3.0

# Input: 10
# Output: 0

# Input: 1 1 1 1 1 66
# Output: 1.0

# Input: 1 1 0 0 11
# Output: 0
