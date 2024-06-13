import contextlib
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtracing(val):
            if len(val) == n:
                result.append(val.copy())
                return

            for num in nums:
                if num not in val:
                    val.append(num)
                    backtracing(val)
                    val.pop()

        backtracing([])

        return result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
        nums = [1,1,2]
        Output: [[1,1,2],[1,2,1],[2,1,1]]
        """

        result = []
        n = len(nums)
        nums.sort()

        def backtrack(val: List[int], used: List[bool]):
            if len(val) == n:
                result.append(val.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                num = nums[i]

                # handle dupliacate
                if i >= 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                val.append(num)
                used[i] = True
                backtrack(val, used)
                val.pop()
                used[i] = False

        used = [False for n in nums]
        backtrack([], used)

        return result


nums = [1, 1, 2]
nums1 = [1, 2, 3]
sol = Solution()
val1 = sol.permute(nums1)
val = sol.permuteUnique(nums)
# print(f"permute: {val1}")
print(f"permuteUnique: {val}")
