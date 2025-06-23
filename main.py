# Check what number(s) exits in both files and pick them out

with open("file1.txt") as num1:
    num_list1 = num1.readlines()
    striped_list1 = []
    for num in num_list1:
        list_num = num.strip("\n")
        striped_list1.append(int(list_num))


with open("file2.txt") as num2:
    num_list2 = num2.readlines()
    striped_list2 = []
    for num in num_list2:
        list_num = num.strip("\n")
        striped_list2.append(int(list_num))


result = [num for num in striped_list1 if num in striped_list2]

print(result)

# we can work on this file like this too to get same result with fewer lines of code

with open("file1.txt") as num1:
    num_list1 = num1.readlines()

with open("file2.txt") as num2:
    num_list2 = num2.readlines()

result = [int(num) for num in striped_list1 if num in striped_list2]

print(result)

# That is sweet with List Comprehension
