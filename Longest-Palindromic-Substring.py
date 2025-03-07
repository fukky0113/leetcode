def expand_center(left, right, s):
    while(left >= 0 and right < len(s) and s[left]==s[right]):
        left -= 1
        right += 1
    return s[left+1:right]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        right = 0
        left = 0
        max_str = s[0]

        for i in range(len(s)-1):
            odd = expand_center(i, i, s)
            even = expand_center(i, i+1, s)

            if len(odd) > len(max_str):
                max_str = odd

            if len(even) > len(max_str):
                max_str = even

            print(i, odd, even)
        return max_str
