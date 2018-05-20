# all start-end point O(n^2)
# check palindrome O(n)
# use DP

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N == 0:
            return ''
        dp = []
        maxLength = 1
        maxRow = 0
        maxCol = 0
        for i in range(N):
            dp.append([0] * N)
        for i in range(N):
            dp[i][i] = 1
        for i in range(0, N - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                maxLength = 2
                maxRow = i
                maxCol = i + 1
        for interval in range(2, N):
            for i in range(0, N - interval):
                j = i + interval
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > maxLength:
                        maxRow, maxCol, maxLength = i, j, dp[i][j]

        return s[maxRow:maxCol + 1]


x = Solution()
print(x.longestPalindrome('zbaxz'))
