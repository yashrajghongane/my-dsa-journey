'''
# Problem :- 
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums

Input / Output
• Input: A list of integers, nums.
	• Example: nums = [1, 2, 3, 4]
• Output: A list of integers representing the running sum.
	• Example: [1, 3, 6, 10]

Example :- 
Let's look at a new array: nums = [5, 1, 10, 2]
• The 1st element is just the first number: 5
• The 2nd element is the first + second: 5 + 1 = 6
• The 3rd element is the sum so far + third: 6 + 10 = 16
• The 4th element is the sum so far + fourth: 16 + 2 = 18

# Pseudocode :- 
FUNCTION runningSum(nums):
    FOR i FROM 1 TO length(nums) - 1:
        nums[i] = nums[i] + nums[i - 1]
    RETURN nums

'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
