"""
46. Permutations (Medium)

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique


------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses backtracking to generate all possible permutations:

1. Initialize an empty result list `res` to store all permutations

2. Define a recursive backtrack function with two parameters:
   - `numbers`: remaining numbers to permute
   - `path`: current permutation being built

3. Base case:
   - If `numbers` is empty, we've used all elements
   - Append the complete `path` to `res`
   - Return to explore other branches

4. Recursive case:
   - For each index i in numbers:
     * Take the element at position i as the next element in permutation
     * Recursively call backtrack with:
       - Remaining numbers: numbers[:i] + numbers[i+1:] (all except i-th element)
       - Updated path: path + [numbers[i]] (add current element to path)
     * This explores all permutations starting with numbers[i]

5. Start the backtracking process with the original nums and empty path

Key insight: At each recursive call, we choose one element from the remaining
numbers and explore all permutations of the rest. The slicing creates a new
list without the chosen element, allowing us to explore all possibilities.

Example trace for [1,2,3]:
- Choose 1: permute [2,3] → [1,2,3], [1,3,2]
- Choose 2: permute [1,3] → [2,1,3], [2,3,1]
- Choose 3: permute [1,2] → [3,1,2], [3,2,1]

Time Complexity: O(n! * n)
  - There are n! permutations
  - Each permutation requires O(n) time for list slicing operations
Space Complexity: O(n! * n)
  - Result list stores n! permutations, each of length n
  - Recursion depth is O(n)
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(numbers, path):
            if not numbers:
                res.append(path)
                return None

            for i in range(len(numbers)):
                backtrack(numbers[:i] + numbers[i + 1:], path + [numbers[i]])
            return None

        backtrack(nums, [])
        return res


print(Solution().permute(nums=[1,2,3]))
