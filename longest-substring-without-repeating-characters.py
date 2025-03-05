def str_duplication(input_str):
    return len(input_str) == len(set(input_str))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        start = 0
        end = 0
        roop_cnt = 1
        while(True):
            for i in range(roop_cnt):
                end = s_len + i
                start = end - s_len
                if str_duplication(s[start:end]):
                    return end - start
            s_len -= 1
            roop_cnt += 1
