'''
# Problem :- Given an array of numbers and a target number, find the index of the target. If it does not exist, return -1 

# Psuedo Code 
START
take an arr 
take an target
for each elemenet in arr 
    if arr[index](value) == target 
        return index
    else 
        -1 
END

# Dry - Run
array  = [4, 8, 2, 7, 5]
target = 7

i = 0 
current value = 4
found = no 

i = 1
current value = 8
found = no 

i = 2
current value = 2
found = no 

i = 3
current value = 7
found = Yes 
Return 3
'''
# Normal Version
def find_target(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [4, 8, 2, 7, 5]
print(find_target(arr,7))


# Complexit 
# Time : O(n)
# Space : O(1)

# leetcode version