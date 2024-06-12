from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracing(left, right, val):
            if left == 0 and right == 0:
                result.append(val)

            if left > 0:
                backtracing(left - 1, right, val + "(")
            if right > left:
                backtracing(left, right - 1, val + ")")

        backtracing(n, n, "")

        return result


sol = Solution()
val = sol.generateParenthesis(3)
print(val)
