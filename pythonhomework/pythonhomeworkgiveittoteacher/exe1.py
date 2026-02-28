count=0
num=int(input("Enter a number:"))
while num!=0:
    if num%2==0:
        count=count+1
    num=int(input("Enter a number:"))
print(count)


# Input: 10 20 33 44 0
# Output: 3

# Input: 1 3 5 7 0
# Output: 0

# Input: 2 4 6 8 10 0
# Output: 5 

# Input: 0
# Output: 0

# Input: -2 -4 10 0
# Output: 3
