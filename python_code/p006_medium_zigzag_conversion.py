# assume numRows>0


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        # works when numRows>=2
        result = [[] for _ in range(numRows)]
        up_state, count = True, numRows
        for char in s:
            if up_state:
                result[numRows - count].append(char)
                count -= 1
                if count == 0:
                    up_state = False
                    count = 2
            else:
                result[-count].append(char)
                count += 1
                if count > numRows:
                    up_state = True
                    count = numRows - 1
        return ''.join([''.join(L) for L in result])
