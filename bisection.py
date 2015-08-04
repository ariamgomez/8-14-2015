## This square root calculator will depict the 'Bisection Method'
## to calculate the root and will compare to 'Exhaustive Enumeration' (Brute Force approach)
## Python 2.7.9

# Error
epsilon = 0.01

# Counters
ans = 0.0
count = 0.0

# My algorithmic boundaries
low = 0.0
high = 0.0

x = raw_input ("Please enter a number, we will find its root ")
x = float(x)
# Notice that the max that the ans can be is the square root of x, since we are depicting
# the square root here we will avoid using the square root function itself
# Here's what I mean: epsilon <= x - ans*ans if epsilo is zero, then ans^2 <= x
high = max (x,1)

while epsilon <= abs(x-(ans*ans)):
    ans = (low + high) / 2
    count = count + 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
print ("We tried this many times "), count
print ("The root is"), ans


    





