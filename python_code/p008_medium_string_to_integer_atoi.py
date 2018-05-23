class Solution:
    def myAtoi(self, mystr):
        """
        :type mystr: str
        :rtype: int
        """
        result = 0
        INT_MAX = 2147483647  # 2^31-1 == 2147483647
        INT_MIN = -2147483648  # -2^31 == -2147483648
        mystr = mystr.lstrip(' ')
        negative = False
        for i, char in enumerate(mystr):
            if i == 0 and char == '+':
                continue
            if i == 0 and char == '-':
                negative = True
            elif not char.isdigit():  # use char in '0123456789' make 30% faster
                break
            else:
                result = result * 10 + int(char)
        if negative:
            result = -result
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.myAtoi('   -42'))
