# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        result = []
        for i in range(len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                result.append(sorted_nums[i])
        return result
        