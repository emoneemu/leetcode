"""
problem number 22 :Generate parentheses

problem statement:

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(curr, open_cnt, close_cnt):
            # If the string is complete, record it
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # We can add '(' if we still have some left to place
            if open_cnt < n:
                backtrack(curr + "(", open_cnt + 1, close_cnt)

            # We can add ')' only if it won't break validity
            if close_cnt < open_cnt:
                backtrack(curr + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res