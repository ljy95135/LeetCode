# use re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        p = '^' + p + '$'
        p = re.compile(p)
        m = p.match(s)
        return m is not None
