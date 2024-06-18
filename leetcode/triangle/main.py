from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Given a triangle array, return the minimum path sum from top to bottom.
        For each step, you may move to an adjacent number of the row below.
        More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

        subproblem: for index[i][j] whats their minimum path sum.
        """

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


sol = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
# triangle = [[-1], [2, 3], [1, -1, -3]]
val = sol.minimumTotal(triangle)
print(val)
