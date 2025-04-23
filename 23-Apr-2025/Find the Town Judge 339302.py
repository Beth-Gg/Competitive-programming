# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusters = [x[0] for x in trust]
        # print(trusters)
        potential_judge = -1
        for i in range(1, n + 1):
            if i not in trusters:
                potential_judge = i

        for j in range(1, n + 1):
            if j != potential_judge and [j, potential_judge] not in trust:
                return -1
        
        return potential_judge 
        
        