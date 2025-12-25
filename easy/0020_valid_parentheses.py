"""
20. Valid Parentheses (Easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


------------------------------------------------------------------------------------------
Solution Explanation:
This problem is solved using a stack data structure. Two implementations are provided:

Solution 1 (with custom Stack class):
- Implements a custom Stack class with push, pop, peek, is_empty, and size methods
- Uses a dictionary to map opening brackets to their corresponding closing brackets
- Algorithm:
  1. Iterate through each character in the string
  2. If it's a closing bracket ')]}': check if it matches the top of stack
  3. If it's an opening bracket '([{': push to stack
  4. At the end, stack should be empty for valid parentheses

Solution 2 (with Python list):
- Uses Python's built-in list as a stack (more Pythonic)
- Same logic but cleaner implementation
- Algorithm:
  1. For closing brackets: check if stack is not empty and top matches
  2. For opening brackets: append to stack
  3. Return True if stack is empty at the end

Key insight: Opening brackets must be closed in the correct order, which is
exactly what a stack (LIFO - Last In First Out) data structure handles.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack in worst case (all opening brackets)
"""

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.is_empty():
      return True
    return self.stack.pop()

  def peek(self):
    if self.is_empty():
      return True
    return self.stack[-1]

  def is_empty(self):
    return self.size() == 0

  def size(self):
    return len(self.stack)


class Solution:
    parentheses_stack = Stack()
    parentheses_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s: str) -> bool:
        for i in s:
            if i in ')]}':
                last_symbol = self.parentheses_stack.peek()
                needed_symbol = self.parentheses_dict[last_symbol]
                if i != needed_symbol:
                    return False
                self.parentheses_stack.pop()
            else:
                self.parentheses_stack.push(i)

        if self.parentheses_stack.is_empty():
            return True
        return False

class Solution_2:

    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for i in s:
            if i in ')]}':
                if not stack:
                    return False
                last_symbol = stack[-1]
                needed_symbol = pairs[last_symbol]
                if i != needed_symbol:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

case = "([])"

print(Solution().isValid(case))
