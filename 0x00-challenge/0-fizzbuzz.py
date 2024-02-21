#!/usr/bin/python3
""" FizzBuzz Challenge
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    iTemp = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            iTemp.append("FizzBuzz")
        elif (i % 3) == 0:
            iTemp.append("Fizz")
        elif (i % 5) == 0:
            iTemp.append("Buzz")
        else:
            iTemp.append(str(i))
    print(" ".join(iTemp))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    iNum = int(sys.argv[1])
    fizzbuzz(iNum)
