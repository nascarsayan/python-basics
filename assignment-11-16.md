### 1: Armstrong number

Input a number from the user, and check if it is an Armstrong number.
An Armstrong number is a number whose sum of cube of digits is equal to the number itself.

Example:
```
153 = (1*1*1) + (5*5*5) + (3*3*3)
153 = 1 + 125 + 27
153 = 153
```

`input()`: To ask input from user

`isdigit()`: To check if input is a number

`int()`: To convert string to integer

To get the individual digits, keep on diving by 10 till it is 0. You cube each digit and save the sum.

### 2: Perfect number

A Perfect number is a number which is equal to sum of its proper divisors.
A proper divisor is any divisor < number.

Example:
```
28 = 1 + 2 + 4 + 7 + 14
```