"""
21. Merge Two Sorted Lists (Easy)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order


------------------------------------------------------------------------------------------
Solution Explanation:
This solution uses a recursive approach to merge two sorted linked lists:

1. Base case: If one list is empty, return the other list
   - If not list1 or not list2: return list1 or list2

2. Recursive case: Compare the values of the current nodes
   - If list1.val < list2.val:
     * Current node is list1
     * Recursively merge list1.next with list2
     * Set list1.next to the result of the merge
     * Return list1
   - Otherwise:
     * Current node is list2
     * Recursively merge list1 with list2.next
     * Set list2.next to the result of the merge
     * Return list2

Key insight: At each step, we choose the smaller node and recursively merge
the rest. The recursion naturally handles all the pointer updates.

Time Complexity: O(n + m) where n and m are the lengths of the two lists
Space Complexity: O(n + m) due to recursion call stack
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: list) -> Optional[ListNode]:
    """
    Helper function to create a linked list from a Python list.

    Args:
        values: List of integers to convert to linked list

    Returns:
        Head node of the created linked list, or None if input list is empty

    Example:
        >>> head = create_linked_list([1, 2, 4])
        >>> # Creates: 1 -> 2 -> 4 -> None
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head: Optional[ListNode]) -> None:
    """
    Helper function to print a linked list in readable format.

    Args:
        head: Head node of the linked list to print

    Example:
        >>> head = create_linked_list([1, 2, 4])
        >>> print_linked_list(head)
        1 -> 2 -> 4 -> None
    """
    values = []
    current = head

    while current:
        values.append(str(current.val))
        current = current.next

    print(" -> ".join(values) + " -> None")


class Solution:
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# Example usage:
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

result = Solution().mergeTwoLists(list1, list2)
print_linked_list(result)
