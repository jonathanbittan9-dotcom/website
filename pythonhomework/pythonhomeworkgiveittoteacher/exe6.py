count=0
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
max_num1 = num1
max_num2 = num2
count=count+1
while (num1+num2)%2==0:
    sum1=num1+num2
    if num1+num2 > max_num1+max_num2:
        max_num1=num1
        max_num2=num2
    count=count+1   
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
print("The number of pairs is:",count-1)
print("The largest sum is of pair:",max_num1, max_num2)


# Input: 2 4, 6 8, 1 3, 1 2
# Output: The number of pairs is: 3
#         The largest sum is of pair: 6 8

# Input: 1 3, 5 7, 9 11, 2 4, 4 3
# Output: The number of pairs is: 4
#         The largest sum is of pair: 9 11

# Input: 0 0, 1 2
# Output: The number of pairs is: 1
#         The largest sum is of pair: 0 0

# Input: -2 -2, 2 2, 1 2
# Output: The number of pairs is: 2
#         The largest sum is of pair: 2 2
