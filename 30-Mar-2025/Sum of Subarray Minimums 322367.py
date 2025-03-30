# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        stack = []
        ans = 0
        for idx, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                popped = stack.pop()
                left = popped[0] + 1
                if stack:
                    left = popped[0] - stack[-1][0]
                right = idx - popped[0]
                print(left, right)
                ans += popped[1] * left * right

            stack.append((idx, num))
        
        for i in range(len(stack)):
            if i > 0:
                left = stack[i][0] - stack[i - 1][0]
            else:
                left = stack[i][0] + 1
            right = len(arr) - stack[i][0]
            print(left, right)
            ans += stack[i][1] * left * right

        return ans % ((10 ** 9) + 7)


        # ans = 0
        # for i in range(len(arr)):
        #     prev_min_idx = -1
        #     next_min_idx = len(arr)
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] < arr[i]:
        #             next_min_idx = j
        #             break
        #     for k in range(i - 1, -1, -1):
        #         if arr[k] < arr[i]:
        #             prev_min_idx = k
        #             break

        #     n = next_min_idx - prev_min_idx - 1
        #     print(prev_min_idx, next_min_idx)
        #     print(arr[i], n)
        #     ans += arr[i] * (n * (n + 1) // 2)
            
        # return ans

            



        # total = 0


        # for i in range(len(arr)):
        #     minn = arr[i]
        #     for j in range(i, len(arr)):
        #         minn = min(minn, arr[j])
        #         total += minn

        # # print(total)
        # return total % ((10 ** 9) + 7)
        