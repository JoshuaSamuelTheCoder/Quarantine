class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        num = x if x > 0 else -x

        ret_val = 0


        while num != 0:
            d, r = num //10, num % 10
            ret_val = ret_val*10 + r
            num = d

        if ret_val > 2**31-1:
            return 0


        return ret_val if x > 0 else -ret_val
            
