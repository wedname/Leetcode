"""
28. Find the Index of the First Occurrence in a String (Easy)

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters


------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses a sliding window approach:

1. Calculate the valid range: len(haystack) - len(needle) + 1
   - We can't start searching beyond this point as there wouldn't be enough
     characters left to match the needle

2. Iterate through each possible starting position in haystack
   - For each position i, extract a substring of length equal to needle
   - Use slicing: haystack[i:i+len(needle)]

3. Compare the substring with needle
   - If they match, return the current index i
   - If no match found after checking all positions, return -1

Key insight: We only need to check positions where there are enough characters
left to potentially match the entire needle string.

Time Complexity: O(n * m) where n = len(haystack) and m = len(needle)
                 In worst case, we compare the entire needle at each position
Space Complexity: O(1) - only using variables for iteration
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


print(Solution().strStr(haystack="hello", needle="ll"))
