class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        left = 0
        right = len(str_x) - 1

        while(str_x[left] == str_x[right]):
            left += 1
            right -= 1
            if (left >= right):
                return True
        return False
