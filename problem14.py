"""
Problem 14 Longest Common Prefix

problem statement:
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

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # The LCP of the whole array equals the LCP of the min and max strings (lexicographically)
        s1, s2 = min(strs), max(strs)
        i = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return s1[:i]
            i += 1
        return s1[:i]