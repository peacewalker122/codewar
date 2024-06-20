#include <algorithm>
#include <iostream>
#include <ostream>
#include <vector>

using namespace std;

class Solution {
public:
  // You are given an integer array nums. You are initially positioned at the
  // array's first index, and **each element in the array represents your
  // maximum jump length at that position**. Return true if you can reach the
  // last index, or false otherwise. nums = [2,3,1,1,4]
  bool canJump(vector<int> &nums) {
    int n = nums.size();
    int maxreach = 0; // this is to know how much we could achieve

    for (int i = 0; i < n; i++) {
      if (i > maxreach) {
        return false;
      }

      maxreach = max(maxreach, i + nums[i]);
    }

    return maxreach >= nums.size() - 1;
  }
};

int main(int argc, char *argv[]) {
  auto sol = Solution();
  std::vector<int> nums = {2, 0, 0}; // Example master data
  bool result = sol.canJump(nums);
  std::cout << "Can Jump? " << result << std::endl;
  return 0;
}
