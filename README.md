# Programming Boot Camp

**Goal**: By the end of this boot camp you will know the basics of programming, the current debates in comp sci, your role in your company, and have three ideas for what your startup will do or create.

**Language**:
Python will be used for the following reasons: 
- [reason one](https://stackoverflow.blog/2017/09/14/python-growing-quickly/) 
- [reason two](https://stackoverflow.blog/2017/09/06/incredible-growth-python/). 

You may, however, use [p5js](https://p5js.org/). P5js is best suited for those who wish to visualize (art people looking at you). Please see the teacher if you wish to use p5js.

# Playlist for Startup Boot Camp

| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Make how-to guides for programs 0 and 1     | [check list](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/how_to_things.md)
| Complete labs 1 - 3                         | Design, program, and comment your own unique programs
| Pick your group role                        | How will you help in a team
| Product research                            | What is your startup's product or service
| Debate Topic                                | Prepare for debate
| Teacher Check-ins                           | Minimum three per group

# Links:

| What                                        | Link         
| --------------------------------------------|------------------------------------------------------------------------------
| Mr. James meeting sign up                   | [link]("#")
| Mr. Moran meeting sign up                   | [link]("#")
| Mrs. Ju meeting sign up                     | [link]("#")
| Mr. New Guy sign up                         | [link]("#")
| Python FAQ                                  | [link]("#")
| P5JS FAQ                                    | [link]("#")

# Debate
[source](http://www.csun.edu/~dgw61315/debformats.html#policy)

Team policy debate is the oldest, and still probably the most popular, format of debate practiced in American high schools.  The proposition side is called the Affirmative or Aff, and the opposition side is called the Negative or Neg.  Each side is a team composed of two debaters, so that there are four people participating in the debate (not including the judge and audience). 

#### Format  
Our round of team policy debate consists of four speeches.  The first two speeches are called constructive speeches, because the teams are perceived as laying out their most important arguments during these speeches.  The last two speeches are called rebuttals, because the teams are expected to extend and apply arguments that have already been made, rather than make new arguments.

- The affirmative team both begins and ends the debate
- The negative side will have two speechs in a row
- Every person will not present during the debate as a team will only have two debaters
- This tasks is meant for those who enjoy theory and policy of technology rather than programming
- Constructive speechs are eight minutes
- Rebuttals are four - eight minutes

#### Debate Topics
- [Not Everyone Should Code](https://www.youtube.com/watch?v=EFwa5Owp0-k)
- [The Singularity](https://www.newyorker.com/magazine/2018/05/14/how-frightened-should-we-be-of-ai)


![doggo](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/IgnDYD9.gif)

# Programming Cheat Sheet

### How to Run a Program

![file path pic](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/0/filepath.png)

[p5js run a program](https://p5js.org/get-started/)


**File Path**
A path, the general form of the name of a file or directory, specifies a unique location in a file system. A path points to a file system location by following the directory tree hierarchy expressed in a string of characters in which path components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash ("/"), the backslash character ("\"), or colon (":")


### Variables
Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program. [source](https://launchschool.com/books/ruby/read/variables)

Typically, a program consists of instruction s that tell the computer what to do and data that the program uses when it is running

### Assigning Value to Variables
There are four primary data types in programming:

| Data type     | Example       | Assigning    |
| ------------- |:-------------:| ------------:|
| int           | 110           | a = 30       |
| float         | 110.010101    | a = 1.0101   |
| boolean       | True or False | tacos = true |
| string        | "words"       | hi = 'hello' |

In computer science and computer programming, a data type or simply type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. [source](https://en.wikipedia.org/wiki/Data_type)

### Control Flow

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. [source](https://en.wikipedia.org/wiki/Control_flow)

#### Diagram of Control Flow

![pic](https://upload.wikimedia.org/wikipedia/commons/0/06/For-loop-diagram.png)

### Types of Control Flow
There are many ways to control your program. Here, we will go over the most commonly used. It is important to remember that there are many ways to write a program, however, we will seek for the best.

### Choice: If/Else statements
![pic1](https://i.imgur.com/xNWld3g.jpg)

The if statement checks for a condition and executes the proceeding statement or set of statements if the condition is 'true'.

```python
# assign an int to a variable called a
a = 5

# begin choice control flow
if a > 10:
  print("I'm greater than 10")
elif a < 0:
  print("I am in the red")
# you can have endless elif statements
else:
  print("I am smaller than 10")
  
```

### Operators
When controlling how a program runs, operators help define conditionals. If x > 10, if y == x, etc.

#### Relational Operator
Operator     | Meaning 
------------ | ------------
x == y | (x is equal to y)
x != y | (x is not equal to y)
x <  y | (x is less than y)
x >  y | (x is greater than y)
x <= y | (x is less than or equal to y)
x >= y | (x is greater than or equal to y)


#### Arithmetic Operator

Operator     | Meaning 
------------ | ------------
x + y  | Adds values on either side of the operator
x - y  | Subtracts right hand operand from left hand operand
x * y  | Multiplies values on either side of the operator
x / y  | Divides left hand operand by right hand operand
x % y  | Modulus Divides left hand operand by right hand operand and returns remainder
x ** y | Performs exponential (power) calculation on operators


### Loops
A loop is a way to repeat a portion of code until a condition is met. For example, imagine having to read through a 1000 page expense report to find all costs above $10,000. A loop could do that for you. Or what if you had to make 1000 tacos? A loop could do that too.

![pic2](https://res.cloudinary.com/teepublic/image/private/s--MmSBmzkg--/t_Preview/b_rgb:262c3a,c_lpad,f_jpg,h_630,q_90,w_1200/v1496757724/production/designs/1649527_1.jpg)


```python
# go through every element in num, which will be called x, and print if it is even

for x in num:
  if x % 2 == 0:
    print(x, " is even")
  else:
    print(x, " is odd")
    
```
in this example x is the iterator. That is the variable which changes value. Meaning, if I have a list = [1,2,3,4] x will first equal 1, then the program will check if 1 is even or odd, and print the result. Then x will equal 2, etc...


```python

n = 0
count = 99

while count < n:
 print(count, "bottles of coke on the wall")
  count = count - 1

```
