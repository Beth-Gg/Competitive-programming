# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        perimeter = 0

        def inbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # count = 0
                if grid[row][col] == 1:
                    for rc, cc in directions:
                        new_row = row + rc
                        new_col = col + cc
                        if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                            perimeter += 1
        
        return perimeter
