from typing_extensions import List


class Solution:
    digit_to_char = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return

            chars = self.digit_to_char[digits[index]]

            for c in chars:
                backtrack(index + 1, path + c)

        backtrack(0, "")
        return result


sol = Solution()
val = sol.letterCombinations("23")
print(val)
