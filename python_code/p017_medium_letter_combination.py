class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '' or digits is None: return []
        from itertools import product
        # print(list(product('AB', '12')))  # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
        num_letter_dict = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        letter_list = [num_letter_dict[digit] for digit in digits]
        result = product(*letter_list)
        return [''.join(tup) for tup in result]


if __name__ == '__main__':
    x = Solution()
    print(x.letterCombinations('23'))
