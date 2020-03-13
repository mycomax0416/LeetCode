class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        end = len(s)
        for idx in range(end):
            words = []
            while idx < end:
                if s[idx] not in words:
                    words.append(s[idx])
                else:
                    break
                idx += 1
            ans = max(ans, len(words))
        return ans