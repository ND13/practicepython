def bin_search(num_list, num):
    half_num_list = 1
    
    while half_num_list >= 1:

        half_num_list = len(num_list) // 2
       
        print(num_list, half_num_list)

        if (num == num_list[half_num_list]):
            return True
        elif (num < num_list[half_num_list]):
            num_list = num_list[:half_num_list]
        elif (num > num_list[half_num_list]):
            num_list = num_list[half_num_list:]
    return False

def main():
    num_list = [2, 3, 6, 7, 9, 18, 25, 36, 47, 85, 89, 100, 101]
    num = 6

    found = bin_search(num_list, num)

    if found:
        print('Number exists in array')
    else:
        print('Number does not exist in array')

if __name__ == '__main__':
    main()
