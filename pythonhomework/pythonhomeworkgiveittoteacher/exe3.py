count=0
num=int(input("Enter a number:"))
if num<0:
    num=num*-1
while num!=0: 
    if num%2==0:
        count=count+1
    num=num//10
if  count==0:
    print(0)
else:
    print(count)

# Input: 10203040
# Output: 6

# Input: 13579
# Output: 0

# Input: 24680
# Output: 5

# Input: -123456
# Output: 3
