class Solution:
    def myAtoi(self, s: str) -> int:
        ret = ""
        blank_flag = True
        sign_flag = True

        for word in s:
            if blank_flag and word == " ":
                continue
            blank_flag = False

            if sign_flag and (word == "-" or word == "+"):
                ret += word
                sign_flag = False
                continue
            sign_flag = False

            if word.isdecimal():
                ret += word
            else:
                break
        if not ret or ret == "-" or ret == "+":
            ret = "0"

        int_ret = int(ret)
        if -2 ** 31 >= int_ret:
            int_ret = -2 ** 31
        if int_ret >= 2 ** 31 - 1:
            int_ret = 2 ** 31 - 1
        
        return int_ret

