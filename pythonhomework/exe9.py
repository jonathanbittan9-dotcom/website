count=0
prev = float(input("Enter a number:"))
num = float(input("Enter a number:"))

while num >= prev:
    prev = num
    num = float(input("Enter a number:"))
    count=count+1

print(count)
