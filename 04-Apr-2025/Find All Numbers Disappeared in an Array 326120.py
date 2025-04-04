# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        idx = 0
        while idx < l:
            position = nums[idx] - 1
            print(idx, position)
            if position != idx and nums[position] == nums[idx]:
                idx += 1
            elif position != idx:
                nums[position], nums[idx] = nums[idx], nums[position]
            else:
                idx += 1
        print(nums)
        result = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                result.append(i + 1)

        return result
        