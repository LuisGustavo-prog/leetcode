# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution(object):
    def longestConsecutive(self, nums): # 0(n)
        set_nums = set(nums)
        longest_sequence = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                current_number = num
                sequential_counter = 1

                while (current_number + 1) in set_nums:
                    sequential_counter += 1
                    current_number += 1

                if sequential_counter > longest_sequence:
                    longest_sequence = sequential_counter

        return longest_sequence

sol = Solution()
print(sol.longestConsecutive(nums = [100,4,200,1,3,2])) # output 4
print(sol.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) # Output: 9
