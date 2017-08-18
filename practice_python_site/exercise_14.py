
#could generate a random list here, but easier to use static values
a = [1,1,2,2,3,3]

#takes a list, changes it into a set and takes that set and converts it back to a list
def remove_duplicates(new_list):
	new_list = set(new_list)
	new_list = list(new_list)
	return new_list

print(remove_duplicates(a))