sum=0
num=int(input("Enter a number:"))
while num!=-1:
    if num%2==0 and num%3==0:
        sum=sum+num
    num=int(input("Enter a number:"))
print(sum)


# Input: 6 12 15 18 -1
# Output: 36

# Input: 3 5 7 9 -1
# Output: 0

# Input: 30 45 60 75 -1
# Output: 90

# Input: 2 4 6 8 -1
# Output: 6

# Input: -6 -12 -18 -1
# Output: -36

# Input: 0 -1
# Output: 0