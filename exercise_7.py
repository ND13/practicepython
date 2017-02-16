a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#understanding how to use if statement in a list comprehension is key here 
b = [num for num in a if num % 2 == 0]
print(b)