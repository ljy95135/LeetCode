# carefully read the requirement
# or just compute 2**31 = 2147483648 to make it a litte faster
# int can handle 012 so do not rstrip

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        low_bound = -2 ** 31
        high_bound = -low_bound - 1
        if x == 0:
            return 0
        if x < 0:
            return -self.reverse(-x)
        result = int(str(x).rstrip('0')[::-1])
        return result if low_bound < result < high_bound else 0
