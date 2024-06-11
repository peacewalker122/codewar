from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracing(pos, val: List[int], cumulative_sum):
            if cumulative_sum == target:  # basecase
                result.append(val.copy())
                return
            if cumulative_sum > target:
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue

                val.append(candidates[i])
                backtracing(i + 1, val, cumulative_sum + candidates[i])
                val.pop()

        backtracing(0, [], 0)

        return result


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
sol = Solution()
val = sol.combinationSum2(candidates, target)
print(val)
