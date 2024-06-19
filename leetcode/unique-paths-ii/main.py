from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
        The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
        An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

        Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
        The testcases are generated so that the answer will be less than or equal to 2 * 109.

        subcase: uniquepath for index[i]
        """
        h, w = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 and obstacleGrid[h - 1][w - 1] == 1:
            return 0

        dp = [[0] * w for _ in range(h)]

        dp[0][0] = 1

        for i in range(h):
            for j in range(w):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[h - 1][w - 1]


sol = Solution()
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 1], [0, 0]]

val = sol.uniquePathsWithObstacles(obstacleGrid)
print(f"unique_path: {val}")
