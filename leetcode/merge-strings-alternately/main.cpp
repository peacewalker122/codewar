#include <string>
using namespace std;

class Solution {
public:
  string mergeAlternately(string word1, string word2) {
    int i = 0;
    string result;

    for (; i < word1.size() && i < word2.size(); i++) {
      result += word1[i];
      result += word2[i];
    }

    for (; i < word1.size(); i++) {
      result += word1[i];
    }

    for (; i < word2.size(); i++) {
      result += word2[i];
    }

    return result;
  }
};
