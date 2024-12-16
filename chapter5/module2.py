import module1

# modify both module1 and module 2 so that all code is contained within functions.
print("Running module 2 as {}".format(__name__))

module1.print_name() # This will use the print name function of module1, and since we specified in module1 that it should tell us whether it's run as main or as an import, then we'll know
