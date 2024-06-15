class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
        The test cases are generated so that the answer will be less than or equal to 2 * 109.
        """
        result = [1] * n

        for i in range(m - 1):
            arr = [1] * n
            for j in range(n - 2, -1, -1):
                arr[j] = arr[j + 1] + result[j]
            result = arr

        return result[0]


sol = Solution()
val = sol.uniquePaths(3, 2)
print(val)
