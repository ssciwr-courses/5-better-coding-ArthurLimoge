# not using context manager
# change the below code to use context manager
f = open("data/efield.t","r")
numbers = f.read()
f.close()

# using context manager, we can do the above quicker:
with open("data/efield.t","r") as f:
    numbers = f.read()

# With this context manager, the context is released as soon as you release the manager. Which is why you don't need to close

# for example for threads, databases, etc - for improved resource handling