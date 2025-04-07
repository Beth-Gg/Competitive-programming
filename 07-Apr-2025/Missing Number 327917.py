# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count_nums = Counter(nums)
        print(count_nums)

        for i in range(n + 1):
            if i not in count_nums:
                return i


        