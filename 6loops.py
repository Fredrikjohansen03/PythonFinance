# 6loops.py

# 6.1 For Loops

fruits = ["kiwi", "banana", "cherry"]

# 6.1.1 Use a for loop to loop through the items in the fruits list and print each item.
# TODO: Write your code below
for fruit in fruits:
    print(fruit)
#Output:
#kiwi
#banana
#cherry

# 6.1.2 In the for loop to loop through the items in the fruits list,  when the item value is "banana", jump directly to the next item.
# TODO: Write your code below
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
#Output:
#kiwi
#cherry

# 6.1.3 In the for loop to loop through the items in the fruits list, exit the loop when the item is "banana".
# TODO: Write your code below
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
#Output:
#kiwi

# 6.1.4 Using the Python range() function, create a sequence of numbers from 0 to 5, and print each item in the sequence in a new line:
# HINT: https://www.w3schools.com/python/ref_func_range.asp
# TODO: Write your code below
for num in range(6):
    print(num)
#Output:0, 1, 2, 3, 4, 5