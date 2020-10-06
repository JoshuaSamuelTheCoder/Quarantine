"""
Given a number n, for each integer i in  the range from 1 to n inclusive, print one value per line as follows:

If i is a multiple of both 3 and 5, print FizzBuzz
If i is a multiple of 3 but not 5, print Fizz
If i is a multiple of 5 but not 3, print Buzz
If i is not a multiple of 3 or 5, print the value of i

Input:
int n: upper limit of values to test (inclusive)
Output:
Returns None
Prints appropriate response for each value i in the set {1,2,..,n} in ascending order, each on a separate line.
"""

def divides(n, i):
    return n % i == 0

def fizzBuzz(n):
    for i in range(1, n+1):
        if divides(i, 3) and divides(i, 5):
            print("FizzBuzz")
        elif divides(i, 3):
            print("Fizz")
        elif divides(i, 5):
            print("Buzz")
        else:
            print(i)
