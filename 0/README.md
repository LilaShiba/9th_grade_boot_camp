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


### Playlist:

| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Code the guessing game                      | Follow the walk-a-long
| Design/Diagram your own game                | Create logic of game and diagram control flow
| Have game approved by teacher               | See teacher
| Create Game                                 | Program, comment out code, and use FAQ for questions
| Beta Test                                   | Have users try your game. Come up with how to make better


### Game Checklist:
Your game should use the following:
- use if/else statement
- use loop
- use a variable that changes, while game is played or when a new game is started

# Game Walk-a-long

### Full Example:
![guessing_game](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/0/guess.png)

### Logic Diagram
![diagram](http://www.cs.kent.edu/~ssteinfa/classes/prog.sp06/topics/ch3/flowchart.gif)

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
### Program Ideas:

- Madlibs
- Age Guesser
- Convert temp from F to C
- Dice Roller
- Magic 8 Ball
- Buzzfeed quiz (what type of dog are you)
- etc


