# dict to hold board spot and value
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# method to print board
def printBoard(board):
    # calling each key:value pair to print in order
   print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
   # nice little spaces for my board
   print('-+-+-')
   print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
   print('-+-+-')
   print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# method ended. You can tell by the indent
turn = 'X'
# control flow for playing the game
# 9 turns in all (3 * 3 = 9) so this chain of events happens 9 times
for i in range(9):
    # print the board
	printBoard(theBoard)
    # say whos turn it is
	print('Turn for: ' +turn+ ' . Which Space?')
    # gather user input
	move = input()
    # update hash
	theBoard[move] = turn
    # change whos turn it is
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)
