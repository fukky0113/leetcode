class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)            
        rev_str_x = str_x[::-1]
        result = 0
        if (rev_str_x[-1] == '-'):
            result =  int('-' + rev_str_x[0:-1])
        else:
            result = int(rev_str_x)
        print( 2 ** 31 - 1)
        if (-2 ** 31 > result or result > 2 ** 31 -1):
            result = 0
        return result
        
