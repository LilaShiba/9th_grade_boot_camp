# 9th Grade Boot Camp





## Programming Cheat Sheet


##### Variables
Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program. [source](https://launchschool.com/books/ruby/read/variables)

Typically, a program consists of instruction s that tell the computer what to do and data that the program uses when it is running

#### Assigning Value to Variables
There are four primary data types in programming:

| Data type     | Example       | Assigning    |
| ------------- |:-------------:| ------------:|
| int           | 110           | a = 30       |
| float         | 110.010101    | a = 1.0101   |
| boolean       | True or False | tacos = true |
| string        | "words"       | hi = 'hello' |

In computer science and computer programming, a data type or simply type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. [source](https://en.wikipedia.org/wiki/Data_type)

##### Control Flow

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. [source](https://en.wikipedia.org/wiki/Control_flow)

![pic](https://upload.wikimedia.org/wikipedia/commons/0/06/For-loop-diagram.png)

#### Types of Control Flow


##### Choice: If/Else statements
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

##### Operators
When controlling how a program runs, operators help define conditionals. If x > 10, if y == x, etc.

Operator     | Meaning 
------------ | ------------
x == y | (x is equal to y)
x != y | (x is not equal to y)
x <  y | (x is less than y)
x >  y | (x is greater than y)
x <= y | (x is less than or equal to y)
x >= y | (x is greater than or equal to y)

##### Loops
