# assume all(coin>0 in coins)
# no use for coinValue>amount
# dummyHead: make index==coninValue

# modification: amount's length is too long, not go one by one
# min(combin1, combin2, ...)+1
# update len(coins) times


# can be even faster when not use dp but minus biggest coin
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # handle amount = 0 and < 0
        # O(S*n) n is len(coin) and S is amount
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        result = [1 if x in coins else None for x in range(amount + 1)]
        result[0] = -1
        for i, v in enumerate(result):
            if v:
                continue
            for coin_value in coins:  # find smallest combination
                if i - coin_value < 0:  # make sure index not negative, not the syntax meaning
                    continue
                if result[i - coin_value] == -1:
                    continue
                num = result[i - coin_value] + 1
                if result[i] is None or num < result[i]:
                    result[i] = num
            if result[i] is None:
                result[i] = -1
        return result[-1]


if __name__ == '__main__':
    xx = Solution()
    k = xx.coinChange([3, 7, 405, 436], 8839)
    print(k)  # too slow!
