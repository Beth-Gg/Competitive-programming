# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        minn, maxx = 0, max(candies)

        def validator(num):
            count = 0
            if num == 0:
                return True
            for candy in candies: 
                count += candy // num
                # print(num, candy, count)
            if count >= k:
                return True
            return False

        while minn <= maxx:
            mid = (minn + maxx) // 2

            if validator(mid):
                minn = mid + 1
            else:
                maxx = mid - 1

        # print(minn, maxx)
        return maxx
