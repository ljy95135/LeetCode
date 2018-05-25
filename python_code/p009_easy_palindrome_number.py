# or reverse later half of the number is a good idea


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # delete this can be a little faster
        # if x < 0:
        #     return False
        # method 1
        # str_x = str(x)
        # return str_x == str_x[::-1]

        # method 2 a little faster
        str_x = str(x)
        half = len(str_x) // 2
        for i, c in enumerate(str_x):
            if str_x[-i - 1] != c:
                return False
            if i >= half:
                return True
