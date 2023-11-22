1. **What is a variable in programming?**
    - A variable in programming is a symbolic name or identifier that stores a value or data. It acts as a container to hold information that can be referenced and manipulated in a program. Variables can store different types of data such as numbers, strings, or objects.

2. **Explain the difference between 'if' and 'while' statements in programming.**
    - An 'if' statement is a conditional statement used for decision-making in programming. It checks a condition and executes a block of code only if the condition is true. It's used for branching the program's flow.
    - A 'while' statement is a looping construct that repeatedly executes a block of code as long as a specified condition is true. It's used for repetitive tasks where the number of iterations is not known in advance.

3. **What is the purpose of comments in a program?**
    - Comments in a program are used to add explanatory notes or descriptions within the code. They are ignored by the interpreter or compiler and are meant for human readers to understand the code better, document its functionality, or provide context. Comments improve code readability and help other programmers understand the code's logic.

4. **What does the term 'syntax error' mean in programming?**
    - A syntax error in programming occurs when the code violates the syntax rules of the programming language. It means that the structure or format of the code is incorrect according to the language's syntax. Syntax errors prevent the code from being interpreted or executed and need to be fixed before the program can run.

5. **What is the purpose of a loop in programming?**
    - The purpose of a loop in programming is to execute a block of code repeatedly based on a certain condition. Loops help in automating repetitive tasks, iterating over collections of data, and performing operations multiple times without writing the same code repeatedly.

6. **Explain the difference between '==', '=', and '!=' in programming.**
    - '==' is an equality operator used to compare if two values are equal.
    - '=' is an assignment operator used to assign a value to a variable.
    - '!=' is a not-equal-to operator used to check if two values are not equal.

7. **What is the significance of indentation in Python?**
    - Indentation in Python is significant for indicating blocks of code. It defines the structure and scope of code. Proper indentation is required to denote nested blocks, such as within loops, conditional statements, and functions. Incorrect indentation can lead to syntax errors or unintended logic.

8. **What is the 'input()' function used for in Python?**
    - The 'input()' function in Python is used to take user input from the keyboard. It allows the program to pause and wait for the user to enter some data, usually a string, and returns the entered value as a string.

9. **Explain the concept of a 'conditional statement' in programming.**
    - A conditional statement in programming allows the execution of different actions based on whether a specified condition evaluates to true or false. It controls the flow of the program by making decisions. Examples include 'if', 'else if' (or 'elif' in Python), and 'else' statements.

10. **What is the purpose of the 'range()' function in Python? Give an example.**
    - The 'range()' function in Python generates a sequence of numbers. It's commonly used for iterating over a sequence of numbers in loops. It can take arguments to specify the start, stop, and step values of the sequence. For example:
    ```python
    for i in range(1, 5):
        print(i)
    # Output: 1 2 3 4
    ```

11. **Describe the purpose and usage of 'for' and 'while' loops in Python. Give examples for each.**
    - 'for' loop: It iterates over a sequence (such as a list, tuple, string, or range) or an iterable object. It executes a block of code for each element in the sequence.
    ```python
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(fruit)
    # Output: apple banana orange
    ```

    - 'while' loop: It repeatedly executes a block of code as long as a specified condition is true.
    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    # Output: 0 1 2 3 4
    ```
