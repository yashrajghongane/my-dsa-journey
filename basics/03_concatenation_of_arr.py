'''

* Input: A list of integers called nums, which has a length of $n$.
* Output: A brand new list called ans that has a length of $2n$.
* The Rule: The first half of ans should be an exact copy of nums, and the second half of ans should also be an exact copy of nums.


## 2 Tiny Example
Let's track a simple input manually:


* nums = [7, 8] (Length $n = 2$)
* Your target output ans needs to be twice as long ($2n = 4$).
* First pass copies nums elements: [7, 8, _, _]
* Second pass appends them again: [7, 8, 7, 8]


##  Pseudocode (Using Strategy A/B)

FUNCTION getConcatenation(nums):
    Create an empty list called ans
    
    FOR each number in nums:
        Add number to ans
        
    FOR each number in nums:
        Add number to ans
        
    RETURN ans


* Time Complexity: $\mathcal{O}(n)$ because you must look at every element in the input array exactly twice to duplicate it.
* Space Complexity: $\mathcal{O}(n)$ because the newly constructed output array scales directly with the size of the input elements.

'''

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans