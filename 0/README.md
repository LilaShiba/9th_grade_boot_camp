# Programming 101

Goal: To design and create a game that takes in user input.

Roles: Remember the main [playlist](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/README.md). While one or two of your teamates are programming, what else can you be doing?

### Bonus Questions
- what is string interpolation and show two ways to do string interpolation in python.
- find and fix the one programming error in this readme file
- team with most answers in the FAQ gets 5 bonus points
- team with best how-to for this lab and presents to class gets 5 bonus points

## What Are You Working On?
At the end of each class, document what each team member worked on. 

![what](https://thechive.files.wordpress.com/2017/02/you-will-either-love-or-hate-the-new-what-in-tarnation-meme-2.jpg?quality=85&strip=info&w=600)

- Is someone documenting/ creating the how-to program? 
- How is preparing for the debate coming along?
- Research, always research
- stuck on a programing question? Assign that TODO to one person and move along.


# Lab 0 Playlist:
- Keep all materials in one folder on google drive.
- name the folder 0_group name
- Screen shots or txt files of code for walk-a-long, for your own program, for your diagram, etc


| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Code the guessing game                      | Follow the walk-a-long - [p5js walk-a-long](https://www.youtube.com/watch?v=TaN5At5RWH8) For [Circuit Playground](https://github.com/kyle1james/led_art_example) follow using sensor guide
| Design/Diagram your own game                | Create logic of game and diagram control flow
| Have game approved by teacher               | See teacher
| Create Game                                 | Program, comment out code, and use FAQ for questions
| Beta Test                                   | Have users try your game. Come up with how to make better
| Have first debate speech rough draft	      | See teacher to get topic
| First teacher meeting			      | Sign on up
| Ask or Answer three things in FAQ 	      | Use that link!
| Daily task list			      | Name of group member followed by what was done each day.


# Game Walk-a-long

### Logic Diagram
![diagram](http://www.cs.kent.edu/~ssteinfa/classes/prog.sp06/topics/ch3/flowchart.gif)

### Full Example with Comments:
![guessing_game](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/0/guess.png)

### How to Get User Input

In python, getting user data is rather simple. 
First, you want to create a variable to hold your users data:

```python
guess = int(input("Guess a number from 1 to 100: "))

# when the program runs, the user will be prompted in the terminal to type in a number.
# The data will always come back in string form- even if they type a number
# This is why we wrap the input in int() 

```

### How to update User Input
How do we know if the user is correct? We need to have a variable that changes each game which holds the answer


```python
import random  # this lets the computer pick a random number

# Defining variables
# The random number is 1 - 100

n = random.randint(1, 100)
guess = int(input("Guess a number from 1 to 100: "))
```
### A loop to keep it going
Now, we need to keep the user guessing until they get the right answer. The logic is while the user did not guess the right answer keep guessing.

```python
# Loop to keep Guessing

while n != guess:

# here we check the answer to help give clues
	if guess < n:
		print("Think Higher Buddy ")
    # we then ask the user to guess again
		guess = int(input())
	elif guess > n:
		print("Got to get down to get right ")
		guess = int(input("How low do you go? "))
	else:
   # Finally, we leave the game once the user gets the right number
		print("Hurray! You got it! The number was " +str(n))
		print("It took you  " +str(count)+ " times to guess the number")
		break
    
```
# Create Your Game
As above, to finish, you should have:

- a logic diagram for your game
- commented program of your game
- a how-to program your game

### Game Checklist:
Your game should use the following:
- if/else statement
- loop
- a variable that changes, while game is played or when a new game is started
### Program Ideas:
**python**
- Madlibs
- Age Guesser
- Convert temp from F to C
- Dice Roller
- Magic 8 Ball
- Buzzfeed quiz (what type of dog are you)
- etc
**p5js**
- circles change color with number of clicks
- solar system 
- bouncing balls
- [object communication](https://www.youtube.com/watch?v=5Q9cA0REztY)
- [mouse interact](https://www.youtube.com/watch?v=TaN5At5RWH8&t=9s)
- etc

### Nice Job!
![jake](https://media.giphy.com/media/8Ry7iAVwKBQpG/giphy.gif)


