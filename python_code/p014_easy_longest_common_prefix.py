# os.path.commonprefix


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        for group in zip(*strs):
            if group.count(group[0]) == len(group):
                result += group[0]
            else:
                break
        return result


if __name__ == '__main__':
    x = Solution()
    x.longestCommonPrefix(["flower", "flow", "flight"])
    x.longestCommonPrefix(["flower"])
    x.longestCommonPrefix([])
    # import os

    # os.path.commonprefix()
