#defines a function that return True if n is divisible m else False
def is_multiple(n,m):
    return True if n%m == 0 else False

print(is_multiple(20.0,5))

#function to check if n is even without multiplication or division
def is_even(n):
    if n == 0:
        return True
    elif n > 0:
        return is_even(n - 2) if n >= 2 else False
    else:
        return is_even(n + 2) if n <= -2 else False

# Examples
print(is_even(10))   # True
print(is_even(-5))   # False
print(is_even(-6))   # True

#alternate solution
def is_even_shorter(n):
    return True if bin(n)[-1] == '0' else False

print(is_even_shorter(10))   # True
print(is_even_shorter(-5))   # False
print(is_even_shorter(-6))   # True

#alternate solution
def is_even_shortest(n):
    return n & 1 == 0

print(is_even_shortest(10))   # True
print(is_even_shortest(-5))   # False
print(is_even_shortest(-6))   # True

#min max
def minmax(data):
    min = float('inf')
    max = float('-inf')
    for value in data:
        if value < min:
            min = value
        if value > max:
            max = value
    return min, max

print(minmax([0,1,2,-8]))
    
    
    
