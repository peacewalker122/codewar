from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        """
        # what's the subproblem
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
val = sol.maxSubArray(nums)
print(val)
