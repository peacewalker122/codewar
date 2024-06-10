from typing_extensions import List


class Solution:
    ans = 0

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        """
        NOTE: score for each alphabet were score[i-1].
        the goal were finding sets with a maximum score from the given words that rescpet the rule letters

        NOTE: Approach 1
        backtracing for each words
        rules: it's must inherit their previous "letter_count", if their count equal into 0 then return.
        """
        count = [0] * 26
        letters_count = [0] * 26
        for letter in letters:
            count[ord(letter) - ord("a")] += 1

        def backtrack(words, letters_count, count, position, temp):
            for i in range(26):
                if letters_count[i] > count[i]:
                    # print(chr(ord("a") + i))
                    return
            self.ans = max(temp, self.ans)

            for i in range(position, len(words)):
                for c in words[i]:
                    letters_count[ord(c) - ord("a")] += 1
                    temp += score[ord(c) - ord("a")]

                backtrack(words, letters_count, count, i + 1, temp)

                for c in words[i]:
                    letters_count[ord(c) - ord("a")] -= 1
                    temp -= score[ord(c) - ord("a")]

        backtrack(words, letters_count, count, 0, 0)

        return self.ans


sol = Solution()
words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(
    sol.maxScoreWords(words, letters, score)
)  # Output should reflect the maximum score
