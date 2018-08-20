# Data Structures and Methods

**goal**: To design a program that uses data structures and methods

Roles: Remember the main [playlist](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/README.md). While one or two of your teamates are programming, what else can you be doing?

### Bonus Questions
- what is the difference between abstraction and encapsulation and show two ways either abstraction or encapsulation is done in python.
- What is a better way to structure  data in unit_1. There is one glaring issues.
- team with most answers in the FAQ gets 5 bonus points
- team with best how-to for this lab and presents to class gets 5 bonus points

## What Are You Working On?
At the end of each class, document what each team member worked on. 

![what](https://i.kym-cdn.com/photos/images/original/000/339/764/93e.gif)

- Is someone documenting/ creating the how-to program? 
- How is preparing for the debate coming along?
- Research, always research
- stuck on a programing question? Assign that TODO to one person and move along.


### Lab 1 Playlist:
- Keep all materials in one folder on google drive
- Name the folder 1_group_name

| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Figure out what and how to use Methods      | This should be a part of your how-to for this lab (see readings)
| Figure out what and how to use Data Strc... | This should be a part of your how-to for this lab (see readings)
| Create program from walk-a-long             | Follow the walk-a-long - [p5js walk-a-long](https://www.youtube.com/watch?v=OAcXnzRNiCY) - [Circuit Playground](https://kyle1james.github.io/cp_midi_2018/) program a MIDI
| Design/Diagram your own program             | Create logic of program and diagram control flow
| Have program approved by teacher            | See teacher
| Create Program                              | Program, comment out code, and use FAQ for questions
| Beta Test                                   | Have users try your program. Come up with how to make better
| Have first debate speech done	              | Test speech on two peers. Take notes on their constructive feedback
| Second teacher meeting			                | Sign on up
| Ask or Answer three things in FAQ 	        | Use that link!
| Daily task list			                        | Name of group member followed by what was done each day.

# Readings
These readings will help in your quest. For your language, make sure you know what and how to create/use methods and data structures. You will need to find your own sources as these two readings will not be enough.

#### python
readings:

- [what is a method](https://stackoverflow.com/questions/3786881/what-is-a-method-in-python)
- [really, what is a method](https://automatetheboringstuff.com/chapter3/)
- [what are data structures](https://docs.python.org/3/tutorial/datastructures.html)

Know:

- lists
- dictionary
- how to create and call a method
#### p5js
The coding walk-a-long will answer most of your questions, however, it is a difficult task.

- array
- hash
- how to create and call a method

![pic](http://www.reactiongifs.com/wp-content/uploads/2013/08/hard-life.gif)


# Coding Walk-a-long

## p5js
Choose your own adventure. Comment your code as you build!

- [Art with physics](https://www.youtube.com/watch?v=OAcXnzRNiCY)
- [Art with API data](https://www.youtube.com/watch?v=rJaXOFfwGVw&list=PLRqwX-V7Uu6a-SQiI4RtIwuOrLJGnel0r)
- [Change an image from webcam](https://www.youtube.com/watch?v=nMUMZ5YRxHI)

## Python
**Goal**: We will be building off of everything you learned in the last lab to create a tic-tac-toe game where the user can see the board.


### Diagram
![tic-tac-toe](https://lh3.googleusercontent.com/-kbg8DEwormM/Vzts_f9VpyI/AAAAAAAADs8/-Q5O5JcyYng/tictacstate_thumb%25255B2%25255D.png?imgmax=800)

### Full Example
![tic](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/1/tic.png)

![term](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/1/cmd-l.png)

**data**
```python
# dict to hold board spot and value
# as of the start of the game, each key's value is a blank space
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


# method to print board
# we want this as a method so we don't have to keep writing code to show an
# update game board

def printBoard(board):
    # calling each key:value pair to print in order
   print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
   # nice little spaces for my board
   print('-+-+-')
   print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
   print('-+-+-')
   print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# method ended. You can tell by the indent

# we create a variable turn to keep track of who is going
turn = 'X'

```



**control flow**
```python
# this sets up a loop to repeat in the range of 9 times
for i in range(9):
    # print the board
	printBoard(theBoard)
    # say whos turn it is
	print('Turn for: ' +turn+ ' . Which Space?')
    # gather user input
	move = input()
    # update key:value pair selected with user input
    # variables make life easy!
	theBoard[move] = turn
    # change whos turn it is
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
    #last, print that board!
printBoard(theBoard)

```

# Ideas for Program
- make the tic-tac-toe game better (score, win screen, computer player, etc)
- encrypt method
- music data base
- best food near dwight based on user input (such as weather, price, time) program
- what type of dog should you get


- API calls and represent data as art
- Object interacting with several forces
- Image rendering 
- etc

### Great Job!
![jake1](http://gifimage.net/wp-content/uploads/2017/08/jake-the-dog-gif-4.gif)
