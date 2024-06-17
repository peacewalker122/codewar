class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

        You have the following three operations permitted on a word:
            Insert a character
            Delete a character
            Replace a character

        subproblem:
        to count how many operations occur to change the word1 into word2
        """
        # basecase
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,  # deletion
                        dp[i - 1][j] + 1,  # insertion
                        dp[i - 1][j - 1] + 1,  # substitusion
                    )

        return dp[n][m]


sol = Solution()
val = sol.minDistance("hello", "bella")

print(f"val: {val}")
