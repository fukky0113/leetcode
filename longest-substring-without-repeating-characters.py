class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        left = 0
        right = 0
        max_l = 0
        s_set = set()

        for right in range(s_len):
            if s[right] not in s_set:
                diff = right - left + 1
                if (diff > max_l):
                    max_l = diff
            else:
                while s[right] in s_set:
                    s_set.discard(s[left])
                    left += 1
            s_set.add(s[right])
        return max_l
