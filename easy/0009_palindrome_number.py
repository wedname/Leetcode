"""
9. Palindrome Number (Easy)

Given an integer x, return true if x is a palindrome, and false otherwise.

A palindrome number is a number that reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
- -2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?


------------------------------------------------------------------------------------------
Solution Explanation:
Two approaches are provided:

Approach 1 (with string conversion):
- Convert the number to string and reverse it using slicing [::-1]
- Compare reversed string with original string
- Simple but uses string conversion
Time Complexity: O(n) where n is number of digits
Space Complexity: O(n) for string storage

Approach 2 (without string conversion):
- Handle negative numbers early (they can't be palindromes)
- Reverse the number mathematically by extracting digits using modulo and division
- Extract last digit: digit = x % 10
- Remove last digit: x = x // 10
- Build reversed number: res = res * 10 + digit
- Compare reversed number with original
Time Complexity: O(n) where n is number of digits
Space Complexity: O(1) - only using integer variables
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # With converting the integer to a string
        palindrome_data = str(x)[::-1]
        return palindrome_data == str(x)

    def isPalindrome(self, x: int) -> bool:
        # Without converting the integer to a string
        if x < 0:
            return False

        initial_number = x
        res = 0

        while x != 0:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit

        return initial_number == res


print(Solution().isPalindrome(x=121))
