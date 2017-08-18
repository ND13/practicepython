#first two lists using values from site, third list is empty to hold values
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

#loops both lists, compares values, appends similar to list c
for num in a and b:
	if num == num in a and b:
		c.append(num)
#printing list c for verification
print(c)