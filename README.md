# More Control Flow Practice

## Problem 1: Pascal's Triangle
Pascal's Triangle is a geometric arrangement of numbers where each number is the sum of the two numbers directly above it. The triangle starts with a single number 1 at the top, and each subsequent row is constructed by adding adjacent numbers from the row above.

Here's how Pascal's Triangle looks:

```
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5  10  10   5   1
1   6  15  20  15   6   1
```
As you move down the triangle, each row corresponds to the coefficients of the expanded form of the binomial $(x + y)^n$, where $n$ is the row number starting from 0. The elements in the $n^{th}$ row represent the binomial coefficients for the expansion of $(x + y)^n$, with the first number being the coefficient of $x^n$ and the last number being the coefficient of $y^n$.

Pascal's Triangle has various applications in mathematics, including combinatorics, probability, and algebra.

Write a program, `pascal.py`, that outputs $n$ rows of  Pascal's Triangle.

### Input Specification
A positive integer $n$ representing the number of rows of Pascal's Triangle to generate.

### Output Specification
Output the first $n$ rows of Pascal's Triangle. Each row should be printed on a separate line. For example:

### Sample Input
```
5
```

### Sample Output
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```


<br><br>

## Problem 2: Prime Number Checker
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is only divisible by 1 and itself, and it has exactly two distinct positive divisors.

For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they are only divisible by 1 and themselves. On the other hand, numbers like 4, 6, 8, 9, and 12 are not prime because they have divisors other than 1 and themselves (e.g., 4 is divisible by 2).

Prime numbers play a fundamental role in number theory and have various applications in mathematics and computer science, such as cryptography, prime factorization, and generating random numbers. They are also used in algorithms for optimization and searching.

Write a program, `prime.py`, that checks if a given integer $n$ is a prime number or not.

### Input Specification
A single integer $n$, where $(1 ≤ n ≤ 10^6)$

### Output Specification
Output `Prime` if $n$ is a prime number, and `Not Prime` if not.

### Sample Input
```
17
```
### Sample Output
```
Prime
```

### More Test Cases
You can use the following numbers to test your program.
Prime | Not Prime
--|--
2, 13, 157, 1033, 10009, 999983 | 1, 22, 222, 2222, 22222, 222222