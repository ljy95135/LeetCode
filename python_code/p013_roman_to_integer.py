class Solution:
    def romanToInt(self, s):
        """
        startswith must in reverse order
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        start = 0
        thousands = [('MMM', 3000, 3), ('MM', 2000, 2), ('M', 1000, 1)]
        hundreds = [('CM', 900, 2), ('DCCC', 800, 4), ('DCC', 700, 3), ('DC', 600, 2), ('D', 500, 1), ('CD', 400, 2),
                    ('CCC', 300, 3), ('CC', 200, 2), ('C', 100, 1)
                    ]
        tens = [('XC', 90, 2), ('LXXX', 80, 4), ('LXX', 70, 3), ('LX', 60, 2), ('L', 50, 1), ('XL', 40, 2),
                ('XXX', 30, 3), ('XX', 20, 2), ('X', 10, 1)]
        ones = [('IX', 9, 2), ('VIII', 8, 4), ('VII', 7, 3), ('VI', 6, 2), ('V', 5, 1), ('IV', 4, 2), ('III', 3, 3),
                ('II', 2, 2), ('I', 1, 1)]
        for romans in [thousands, hundreds, tens, ones]:
            for tpl in romans:
                if s.startswith(tpl[0], start):
                    result += tpl[1]
                    start += tpl[2]
                    break
            if start == length: break
        return result
