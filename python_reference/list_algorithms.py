values = [3,93, 1, 20, 0, 7, 12, 17]

#iterate over a list with a for loop
'''print each item'''
def print_all(nums):
    for n in nums:
        print(v)

#count items in a list
def count_evens(nums):
    count = 0
    for n in nums:
        if n%2 == 0:
            count += 1
    return(count)

#sum items in a list
'''sum is a built in python function'''
total = sum(values)

#find the average value in a list
def mean(nums):
    return sum(nums)/len(nums)

#determine if a list has a value
def find(nums, value):
    for n in nums:
        if n == value:
            return True
#min and max of values in a list
'''min and max are built in python functions'''
big = max(values)
small = min(values)


output = find(values, 56)
print(output)
