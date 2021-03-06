# assume all(coin>0 in coins)
# no use for coinValue>amount
# dummyHead: make index==coninValue
from math import ceil


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # handle amount = 0 and < 0
        # O(n^2) n is amount, too slow when amount is huge
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        result = [1 if x in coins else None for x in range(amount + 1)]
        result[0] = -1
        for i, v in enumerate(result):
            if v:
                continue
            for ii in range(ceil(i / 2) + 1):  # find smallest combination
                if result[ii] == -1 or result[i - ii] == -1:
                    continue
                num = result[ii] + result[i - ii]
                if result[i] is None or num < result[i]:
                    result[i] = num
            if result[i] is None:
                result[i] = -1
        return result[-1]


if __name__ == '__main__':
    xx = Solution()
    k = xx.coinChange([3, 7, 405, 436], 8839)
    print(k)  # too slow!
