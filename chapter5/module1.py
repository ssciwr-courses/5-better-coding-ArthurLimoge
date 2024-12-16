# modify both module1 and module 2 so that all code is contained within functions.

print("This will always be printed.")


def print_name():
    print("Module one is {}".format(__name__))


if __name__ == "__main__":
    print("Runs as main")
    print_name()
else:
    print("Runs as import") # This is for when me use this module as an import (look in module2). Then it will read this message
    print_name()
