# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):
    def threeSum(self, nums):
            nums.sort()
            res = list()

            for center in range(len(nums) - 2):
                if nums[center] > 0:
                    break

                if center > 0 and nums[center] == nums[center - 1]:
                    continue

                left, right = center + 1, len(nums) - 1

                while left < right:
                    sum_result = nums[center] + nums[left] + nums[right]

                    if sum_result == 0:
                        res.append([nums[center], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif sum_result < 0:
                        left += 1
                    else:
                        right -= 1

            return res
                    
sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4])) # Output: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum(nums = [0,1,1])) # Output: []
print(sol.threeSum(nums= [0,0,0,0])) # Output: [0, 0, 0]
print(sol.threeSum(nums= [-100,-70,-60,110,120,130,160])) # Output: [[-100,-60,160],[-70,-60,130]]
