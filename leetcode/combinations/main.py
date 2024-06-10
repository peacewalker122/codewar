from typing_extensions import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracing(position, val: List[int]):
            if len(val) == k:
                result.append(val.copy())
                return

            for i in range(position, n + 1):
                val.append(i)
                backtracing(i + 1, val)
                val.pop()

        backtracing(1, [])
        return result


sol = Solution()
res = sol.combine(4, 2)
print(res)
