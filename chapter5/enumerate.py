lunch = ["Pizza", "Salad", "Pasta", "Sushi", "Sandwich"]

# change the below to use enumerate

index = 0
for meal in lunch:
    print(index, meal)
    index += 1

# We can do this with enumerate:
for index, meal in enumerate(lunch):
    print(index, meal)