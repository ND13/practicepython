import random 
 
#creating two random lists using the random module
a = random.sample(range(10), 5)
b = random.sample(range(10), 5)

#printing each list to verify which values they hold
print(a)
print(b)

print(set(i for i in a if i in b))
