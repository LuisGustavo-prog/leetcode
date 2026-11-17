# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from collections import defaultdict

class Solution(object):
    def groupAnagramsv1(self, strs): # Complexidade O(n.klogk)
        anagram_dictionary = {}

        for anagram in strs:
            organized_anagram = ''.join(sorted(anagram))

            if organized_anagram not in anagram_dictionary:
                anagram_dictionary.setdefault(organized_anagram, []).append(anagram)
                continue

            anagram_dictionary[organized_anagram].append(anagram)

        return [y for x, y in anagram_dictionary.items()]

    def groupAnagrams(self, strs):
        anagram_dictionary = defaultdict(list)

        for anagram in strs:
            organized_anagram = ''.join(sorted(anagram))
            anagram_dictionary[organized_anagram].append(anagram)

        return list(anagram_dictionary.values())
    
sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])) # output [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(strs = [""])) # output [[""]]
