"""
14. Longest Common Prefix (Easy)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses a vertical scanning approach:
1. Find the minimum length among all strings to avoid index out of bounds
2. Iterate character by character from position 0 to min_value
3. For each position i:
   - Take the character from the first string as reference (letter = strs[0][i])
   - Check if all other strings have the same character at position i
   - If any string has a different character, return the prefix found so far
   - If all match, add the character to the prefix
4. Return the complete prefix after checking all positions

Key insight: We only need to check up to the length of the shortest string,
as the common prefix cannot be longer than the shortest string.

Time Complexity: O(S) where S is the sum of all characters in all strings
                 In worst case, all strings are identical
Space Complexity: O(1) - only using variables for iteration and prefix string
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_value = min(len(s) for s in strs)
        prefix = ""
        for i in range(0, min_value):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    return prefix
            prefix += letter
        return prefix



strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))
