#include <iostream>
#include <ostream>
#include <vector>

using namespace std;

class Solution {
public:
  // You are given an integer array nums. You are initially positioned at the
  // array's first index, and each element in the array represents your maximum
  // jump length at that position. Return true if you can reach the last index,
  // or false otherwise. nums = [2,3,1,1,4]
  bool canJump(vector<int> &nums) {
    if (nums.size() == 1) {
      return true;
    }
    // what's the subproblem
    // some array were able to jump and some not, so the subproblem were findout
    // those.
    int cur_position = nums[0];

    if (cur_position == nums.size() - 1) {
      return true;
    }

    vector<bool> valid_tojump(nums.size());

    // Assign true to valid_tojump[i] if nums[i] > 0, otherwise false
    for (size_t i = 0; i < nums.size(); ++i) {
      valid_tojump[i] = nums[i] > 0;
    }

    for (int i = cur_position; cur_position < nums.size();) {
      if (valid_tojump[i]) {
        cur_position += nums[i];
        std::cout << cur_position << std::endl;
        i = cur_position;
      } else {
        return false;
      }
    }

    return true;
  }
};

int main(int argc, char *argv[]) {
  auto sol = Solution();
  std::vector<int> nums = {2, 0, 0}; // Example master data
  bool result = sol.canJump(nums);
  std::cout << "Can Jump? " << result << std::endl;
  return 0;
}
