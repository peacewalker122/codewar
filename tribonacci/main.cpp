#include <vector>

std::vector<int> tribonacci(const std::vector<int> &signature, int n) {
  // If n is zero, return an empty vector immediately
  if (n == 0) {
    return {};
  }

  // If n is less than or equal to the length of the signature, return the first
  // n elements of the signature
  if (n <= signature.size()) {
    return std::vector<int>(signature.begin(), signature.begin() + n);
  }

  // Initialize result with the signature
  std::vector<int> result(signature);

  // Calculate the rest of the sequence until the size of result is n
  while (result.size() < n) {
    int next_value = result[result.size() - 3] + result[result.size() - 2] +
                     result[result.size() - 1];
    result.push_back(next_value);
  }

  return result;
}
