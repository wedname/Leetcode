"""
2347. Best Poker Hand (Easy)

You are given an integer array ranks and a character array suits.
You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.


Example 1:
Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"
Explanation: The hand with all the cards consists of 5 cards with the same suit,
so we have a "Flush".

Example 2:
Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
Output: "Three of a Kind"
Explanation: The hand with the first, second, and fourth card consists of 3 cards with
the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.

Example 3:
Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
Output: "Pair"
Explanation: The hand with the first and second card consists of 2 cards with the same rank,
so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".


Constraints:
ranks.length == suits.length == 5
1 <= ranks[i] <= 13
'a' <= suits[i] <= 'd'
No two cards have the same rank and suit.


------------------------------------------------------------------------------------------
Solution Explanation:
This solution checks poker hands in order of priority (best to worst):

1. Check for "Flush" first (highest priority):
   - Convert suits to a set and check if length is 1
   - If all 5 cards have the same suit, it's a Flush

2. Check for "Three of a Kind":
   - Sort the ranks by frequency (using helper function _sort_ranks)
   - _sort_ranks creates a frequency dictionary and sorts numbers by:
     * Primary: frequency (descending) using -freq[x]
     * Secondary: value (ascending) using x
   - After sorting, check if first 3 elements are all the same
   - Use all() function to verify sorted_ranks[0:3] are identical

3. Check for "Pair":
   - Similar to Three of a Kind but check first 2 elements
   - If sorted_ranks[0:2] are the same, it's a Pair

4. Default to "High Card":
   - If none of the above conditions are met

Key insight: Sorting by frequency first ensures that cards with the same rank
are grouped together at the beginning of the sorted list, making it easy to
check for patterns like "Three of a Kind" or "Pair".

Time Complexity: O(n log n) where n = 5 (constant), so effectively O(1)
Space Complexity: O(n) for the frequency dictionary, so effectively O(1)
"""
from typing import List


class Solution:
    @staticmethod
    def _sort_ranks(nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(nums, key=lambda x: (-freq[x], x))
        return sorted_nums

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        sorted_ranks = self._sort_ranks(ranks)

        if all(s == sorted_ranks[0] for s in sorted_ranks[0:3]):
            return "Three of a Kind"
        if all(s == sorted_ranks[0] for s in sorted_ranks[0:2]):
            return "Pair"

        return "High Card"

ranks = [10,10,2,12,9]
suits = ["a","b","c","a","d"]

print(Solution().bestHand(ranks=ranks, suits=suits))
