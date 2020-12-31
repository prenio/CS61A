"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y >0  # You can replace this line!

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    i = int(len(str(n)))
    total=0
    b=0
    while i > 0:
      total=total+int(str(n)[b])
      b+=1
      i-=1
    return total


def repeater(f, n):
    def g(x):
        nonlocal n
        return repeat(f, x, n+1)
    return g


def repeat(f, x, n):
    if n>1:
        f(x)
        return repeat(f, x, n-1)
