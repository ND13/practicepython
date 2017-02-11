name = input('Please enter your name: ')
#both of these variables are converted to ints so we have matching data types in our 'year_til_100' variable
age = int(input('Please enter your age: '))
year = int(input('What year is it: '))
year_til_100 = year + (100 - age)
#concatenating strings here so make sure to convert the 'year_til_100' to a str data type
print('Hello ' + name + ' your age in the year ' + str(year_til_100) + ' is 100!')
