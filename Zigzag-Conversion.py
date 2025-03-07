class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_dic = {}
        count = 1
        sign = 1

        for i in range(len(s)):
            tmp = ""
            if (count in s_dic.keys()):
                tmp += s_dic[count]
            
            s_dic[count] = tmp + s[i]

            if (numRows != 1):
                if (count >= numRows):
                    sign = -1

                if (count <= 1):
                    sign = 1

                count += sign
            else:
                count = 1
        return "".join(list(s_dic.values()))
