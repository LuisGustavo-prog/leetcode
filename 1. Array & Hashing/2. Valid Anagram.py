# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram")) # true
print(sol.isAnagram(s = "rat", t = "car")) # false
