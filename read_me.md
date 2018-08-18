# 9th Grade Boot Camp

Goal: By the end of this boot camp you will know the basics of programming, your role in your company, and have three ideas for what your startup will do or create.

Playlist for Startup Boot Camp

| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Make guide for programming 101              | Create a blog, film, game, program, etc that teaches all topics in bootcamp
| Complete labs 1 - 3                         | Design, program, comment, and add readme to your own unique programs
| Pick your role                              | How will you help in a team
| Product research                            | What is your startup's product or service
| Debate Topic                                | Prepare for debate 


#### Debate Topics
- [Not Everyone Should Code](https://www.youtube.com/watch?v=EFwa5Owp0-k)
- [The Singularity](https://www.newyorker.com/magazine/2018/05/14/how-frightened-should-we-be-of-ai)



## Programming Cheat Sheet

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
    printx, (x, " is odd")
    
```
in this example x is the iterator. That is the variable which changes value. Meaning, if I have a list = [1,2,3,4] x will first equal 1, then the program will check if 1 is even or odd, and print the result. Then x will equal 2, etc...


```python

n = 0
count = 99

while count < n:
 print(count, "bottles of coke on the wall")
  count = count - 1

```
