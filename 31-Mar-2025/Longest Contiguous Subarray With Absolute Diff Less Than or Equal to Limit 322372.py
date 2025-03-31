# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_q = deque()
        max_q = deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1
            res = max(res, r - l + 1)

        return res

        # q = deque()
        # max_len = 0

        # for num in nums:
        #     if deque and deque

        # cur_max = cur_min = nums[0]
        # max_len = 1
        # curr_len = 0
        # lst = []
        # for i in range(1, len(nums)):
        #     if abs(nums[i] - cur_min) > limit or abs(nums[i] - cur_max) > limit:
        #         max_len = max(max_len, len(lst))
        #         lst = []
        #         cur_min = cur_max = nu
        #     if nums[i] > cur_max:
        #         cur_max = nums[i]

