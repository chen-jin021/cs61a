#Lab 1: Expressions and Control Structures"

'''
Q1:
>>> True and 13
True

>>> False or 0
False

>>> not 10
False

>>> not None
True

>>> True and 1 / 0 and False
ZeroDivisionError

>>> True or 1 / 0 or False
True

>>> True and 0
False

>>> False or 1
True

>>> 1 and 3 and 6 and 10 and 15
True

>>> 0 or False or 2 or 1 / 0
True

>>> not 0
True

>>> (1 + 1) and 1
True

>>> 1/0 or True
ZeroDivisonError

>>> (True or False) and False
False



Q2:

>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)

2
1
0
-1




>>> n = 4
>>> while n > 0:
...     n += 1
...     print(n)
4
5
6
7
.
.
.
#Infinite Loop





>>> def go(n):
...     if n % 2 != 0:
...         print(n / 2)
...         return
...     while n > 0:
...         print(n)
...         n = n // 2
>>> go(4)
2 #return None and ends the program

>>> go(5)
5
2
1



>>> zero = 2
>>> while zero != 0:
...    zero = zero // 2
...    print(zero)
1
0



>>> positive = 28
>>> while positive:
...    print("positive?")
...    positive -= 3
positive? #25
positive? #22
positive? #19
positive? #16
positive? #13
positive? #10
positive? #7
positive? #4
positive? #3


>>> positive = -9
>>> negative = -12
>>> while negative:
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3

#This will evaluate None
'''



# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    def square (x):
        return x * x
    def opposite (b):
        return not b

    #composing f n times on x
    i = 0
    result = x
    while i < n:
        result = f(result)
    return result


    
        
    

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    #Option1:
    #how many digits are there
    temp = n
    digits = 0
    while temp != 0:
        temp //= 10
        digits += 1

    sum_n = 0
    while digits > 0:
        sum_n += n % 10
        n //= 10
        digits -= 1

    return sum_n

result = sum_digits (4224)
print(result)
    
'''#Option2:'''
def sum_digits2(n):
    new_n = str(n)
    length = len(new_n)
    list_of_digits = []
    for i in range(length):
        list_of_digits += [int(new_n[i])]
    sum_n = sum(list_of_digits)
    return sum_n
r = sum_digits2(1234567890)
print(r)




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    new_n = str(n)
    length = len(new_n)
    list_of_digits = []
    for i in range(length):
        list_of_digits += [int(new_n[i])]

    #examine if there are adjacent 8s
    flag = False
    for i in range(len(list_of_digits)-1):
        if list_of_digits[i] == 8 and list_of_digits[i+1] == 8:
            flag = True
    return flag

eights = double_eights(80808080)
print("It is",eights,"that there are double 8s in this")





