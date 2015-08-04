## This square root calculator will depict the
## Compare the efficiency between the
## 'Exhaustive Enumeration' (Brute Force) Vs Bisection Method
## Python 2.7.9

# Error
epsilon = 0.01

# Counters
ansE = 0.0
countE = 0.0
ansB = 0.0
countB = 0.0

# My algorithmic boundaries for the Bisection Method
low = 0.0
high = 0.0

x = raw_input ("Please enter a number, we will find its root using the Bisection Method ")
x = float(x)
# Notice that the max that the ans can be is the square root of x, since we are depicting
# the square root here we will avoid using the square root function itself
# Here's what I mean: epsilon <= x - ans*ans if epsilo is zero, then ans^2 <= x
high = x 

while epsilon <= abs(x-(ansB*ansB)):
    ansB = (low + high) / 2
    countB = countB + 1
    if ansB**2 > x:
        high = ansB
    else:
        low = ansB
print ("We tried this many times "), countB
print ("The root is"), ansB


x = raw_input ("Please enter a number, we will find its root using the Brute Force Method ")
x = float(x)


while epsilon <= abs(x-(ansE*ansE)):
    ansE = ansE + 0.001
    countE = countE + 1
print ("We tried this many times "), countE
print ("The root is"), ansE

    





