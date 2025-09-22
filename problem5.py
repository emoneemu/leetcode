"""
5.Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # Preprocess the string to insert '#' between characters
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n
        c = 0
        r = 0

        for i in range(1, n-1):
            # Mirror index
            mirror = 2 * c - i

            # If i is within the current right boundary, use the mirror value
            if i < r:
                p[i] = min(r - i, p[mirror])

            # Attempt to expand palindrome centered at i
            while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
                p[i] += 1

            # If palindrome centered at i expands past r,
            # adjust center and right boundary
            if i + p[i] > r:
                c = i
                r = i + p[i]

        # Find the maximum element in p
        max_len = 0
        center_index = 0
        for i in range(n):
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        # Extract the longest palindrome
        start = (center_index - max_len) // 2
        end = start + max_len
        return s[start:end]