"""
5. Longest Palindromic Substring (Medium)

Given a string s, return the longest palindromic substring in s.

A palindromic string is a string that reads the same forward and backward.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters


------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses the "expand around center" approach to find the longest palindrome:

Key Idea:
A palindrome mirrors around its center. Therefore, a palindrome can be expanded from
its center, and there are only 2n - 1 such centers (n characters + n-1 positions
between characters for even-length palindromes).

Algorithm:
1. For each possible center position in the string:
   - Check for odd-length palindrome (single character center)
   - Check for even-length palindrome (two character center)
   - Keep track of the longest palindrome found

2. Helper function `expand_around_center(s, left, right)`:
   - Takes a potential center (defined by left and right pointers)
   - Expands outward while characters match: s[left] == s[right]
   - Moves left pointer leftward (left - 1) and right pointer rightward (right + 1)
   - Returns the palindromic substring when expansion stops

3. Helper function `get_longest_str(odd, even)`:
   - Compares two palindromes (odd-length and even-length)
   - Returns the longer one along with its length

4. Main loop:
   - Iterate through each index i in the string
   - For odd-length palindromes: expand from (i, i)
   - For even-length palindromes: expand from (i, i+1)
   - Update longest_palindrome if a longer one is found

Example trace for "babad":
- i=0 ('b'): odd="b", even="" → longest="b"
- i=1 ('a'): odd="bab", even="" → longest="bab"
- i=2 ('b'): odd="aba", even="" → longest="bab" (no change)
- i=3 ('a'): odd="aba", even="" → longest="bab" (no change)
- i=4 ('d'): odd="d", even="" → longest="bab"
Result: "bab"

Time Complexity: O(n²)
  - We iterate through n centers
  - Each expansion can take up to O(n) time in worst case
Space Complexity: O(1)
  - Only using a few variables, excluding the output string
"""
from typing import Tuple


class Solution:
    @staticmethod
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    @staticmethod
    def get_longest_str(odd: str, even: str) -> Tuple[str, int]:
        return (odd, len(odd)) if len(odd) > len(even) else (even, len(even))

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''

        for i in range(len(s)):
            odd = self.expand_around_center(s, i, i)
            even = self.expand_around_center(s, i, i + 1)
            string, len_string = self.get_longest_str(odd, even)

            if len(longest_palindrome) < len_string:
                longest_palindrome = string

        return longest_palindrome


print(Solution().longestPalindrome("abb"))
