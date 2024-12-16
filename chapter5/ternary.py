x = 10

# re-write this conditional as a ternary conditional
if x >= 10:
    y = 1
else:
    y = 0

#Can write this quicker:
y = 1 if x >= 10 else 0

print("Original version {}".format(x))