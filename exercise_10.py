import random 
 
#creating two random lists using the random module
a = random.sample(range(10), 5)
b = random.sample(range(10), 5)

#printing each list to verify which values they hold
print(a)
print(b)

#creating a set of values that are shared between the two lists
#using a set instead of a list ensures that none of the shared
#values between the lists will be repeated.
print(set(i for i in a if i in b))
