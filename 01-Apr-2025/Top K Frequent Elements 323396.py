# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        freq_list = sorted(nums_count.values(), reverse=True)[:k]

        result = []
        for key, value in nums_count.items():
            if value in freq_list and key not in result:
                result.append(key)
                print(result)
        return result


        
        