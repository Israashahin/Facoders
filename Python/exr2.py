print("This is Rock Paper Scissors Game")
player1=input("player1,choose one of these Rock Paper Scissors:  ")
player2=input("player2,choose one of these Rock Paper Scissors:  ")

if player1=='Rock' and player2=='Scissors':
    win='player1 wins,,Congratulations'
if player1=='Scissors' and player2=='Paper':
    win='player1 wins,,Congratulations'
if player1=='Paper' and player2=='Rock':
    win='player1 wins,,Congratulations'

if player1=='Scissors' and player2=='Rock':
    win='player2 wins,,Congratulations'
if player1=='Paper' and player2=='Scissors':
    win='player2 wins,,Congratulations'
if player1=='Rock' and player2=='Paper':
    win='player2 wins,,Congratulations'
print(win)
