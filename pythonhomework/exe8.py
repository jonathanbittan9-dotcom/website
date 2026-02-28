d=int(input("Enter a number of numbers::"))
for x in range(d):
    num=int(input("Enter a number:"))
    if num>=0:
        print(num)
    else:
        numpositive=num*-1
        print(numpositive)
