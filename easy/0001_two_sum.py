"""
1. Two Sum (Easy)

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use
the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists


------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses a hash map (dictionary) approach:
1. First pass: Build a hash_map where key is the number value and value is its index
2. Second pass: For each element, calculate needed_num = target - current_value
3. Check if needed_num exists in hash_map and it's not the same element (hash_map[needed_num] != idx)
4. If found, return the pair of indices

Time Complexity: O(n) - two passes through the array
Space Complexity: O(n) - hash map stores all elements
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, value in enumerate(nums):
            hash_map[value] = idx

        for idx, value in enumerate(nums):
            needed_num = target - value
            try:
                if hash_map[needed_num] != idx:
                    return [idx, hash_map[needed_num]]
                else:
                    continue
            except KeyError:
                continue
        return []


solution = Solution()
print(solution.twoSum(nums=[3,2,4], target=6))
