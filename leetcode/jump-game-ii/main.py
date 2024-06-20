from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
        Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

            0 <= j <= nums[i] and
            i + j < n
        Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
        """

        target = len(nums) - 1
        curr_jump = max_end_jump = min_jump = 0

        for i in range(len(nums)):
            max_end_jump = max(max_end_jump, i + nums[i])

            if max_end_jump >= target:
                min_jump += 1
                break

            if i == curr_jump:
                min_jump += 1
                curr_jump = max_end_jump

        return min_jump


sol = Solution()
# nums = [2, 3, 1, 1, 4]
# nums = [2, 3, 0, 1, 4]
# nums = [1, 2, 3]
# nums = [2, 0, 2, 0, 1]
nums = [1, 2]
nums = [2, 1, 1, 1, 1]
nums = [3, 4, 3, 2, 5, 4, 3]
val = sol.jump(nums)
print(f"minimum_jump: {val}")
