count_shir=0
count_lee=0
turn=1
while count_lee<3 and count_shir<3:
    gamble=int(input("Enter heads(0) or tails(1):"))
    if gamble==1:
        if turn%2==1:  # Shir's turn
            count_shir=count_shir+1
        else:              #Lee's turn
            count_lee=count_lee+1
    turn=turn+1
        
    
if count_shir==3:
    print("Shir has won the gamble and will start the game first!")
else:
    print("Lee has won the gamble and will start the game first!")

# Input: 1 0 1 1 0 1 1
# Output: Shir wins and will start first!

# Input: 0 1 0 0 1 0 1 1
# Output: Lee wins and will start first!

# Input: 1 1 1 1 1
# Output: Shir wins and will start first!

# Input: 0 1 0 1 0 1
# Output: Lee wins and will start first!
