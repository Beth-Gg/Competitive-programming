# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        idx = 0
        result = [0]
        while idx < l:
            position = nums[idx] - 1
            if position != idx and nums[position] == nums[idx]:
                result[0] = nums[position]
                idx += 1
                                # break
            elif position != idx:
                nums[position], nums[idx] = nums[idx], nums[position]
            else:
                idx += 1
        print(nums)
        for i in range(l):
            if i + 1 != nums[i]:
                result.append(i + 1)
                break

        return result
        
        