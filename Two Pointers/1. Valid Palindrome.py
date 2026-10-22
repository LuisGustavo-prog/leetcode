# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s: list[str]):
        palindrome_list = [lette for lette in s.lower() if lette.isalnum()]

        left, right = 0, len(palindrome_list) - 1

        while left < right:
            if palindrome_list[left] == palindrome_list[right]:
                left += 1
                right -= 1
                continue

            return False

        return True


sol = Solution()
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama")) # Output: true
print(sol.isPalindrome(s = "race a car")) # Output: false
