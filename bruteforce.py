## This square root calculator will depict the 'Exhaustive
## Enumeration' a brute force approach.
## Python 2.7.9

# Error
epsilon = 0.01

# Counters
ans = 0.0
count = 0.0

x = raw_input ("Please enter a number, we will find its root ")
x = float(x)


while epsilon <= abs(x-(ans*ans)):
    ans = ans + 0.001
    count = count + 1
print ("We tried this many times "), count
print ("The root is"), ans
