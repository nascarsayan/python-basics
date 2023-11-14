"""

Fibonacci

n1 = 0
n2 = 1

k-th number = sum of previous two numbers
n_k = n_(k-1) + n_(k-2)

0 1 1 2 3 5 8 ...
"""

# n1 = 0
# n2 = 1
# n3 = n1 + n2
# n4 = n3 + n2
# n5 = n4 + n3
# n6 = n5 + n4

# print(n1, n2, n3, n4, n5, n6)

## Using loops

# while True:
# do your stuff
# check for condition. If loop completed, break

n1 = 0
n2 = 1

"""
n3 = n1 + n2

And set 
- n1 to n2
- n2 to n3

"""

# Print first 10 fibonacci numbers

# print(n1, end=" ")
# print(n2, end=" ")

print(n1, n2, end=" ")

count = 2

while count < 10:
    n3 = n1 + n2
    print(n3, end=" ")
    count += 1

    n1 = n2
    n2 = n3

    # if count == 10:
    #     break

print()

print(list(range(5)))  # 0, 1, 2, 3, 4

for i in list(range(5)):
    print(i, end=" ")

# range(3) will return an iterable object
# every iterable object can be converted to a list
print()

# range(2, 10) => 2, 3, 4, 5, 6, 7, 8, 9

# range(5) === range(0, 5)
# range(2, 10, 3) => 2, 5, 8

# range(start, end, step)

## Impl 2

# n1 = 0
# n2 = 1
n1, n2 = 0, 1
print(n1, n2, end=" ")

for i in range(2, 10):
    n3 = n1 + n2
    print(n3, end=" ")

    # n1 = n2
    # n2 = n3
    n1, n2 = n2, n3

print()