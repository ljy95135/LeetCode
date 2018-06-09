class Solution:
    # time limit exceeded
    # if we sort nums at first then no need to sort tuple
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     rst = []
    #     test = set()
    #     length = len(nums)
    #     for i, n in enumerate(nums):
    #         want = -n
    #         want_set = set()
    #         for j in range(i + 1, length):
    #             x = nums[j]
    #             if x in want_set:
    #                 ans = tuple(sorted((x, want - x, -want)))
    #                 if ans not in test:
    #                     rst.append(list(ans))
    #                     test.add(ans)
    #             else:
    #                 want_set.add(want - x)
    #     return rst

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rst = []
        test = set()
        length = len(nums)
        for i, n in enumerate(nums):
            want = -n
            want_set = set()
            for j in range(i + 1, length):
                x = nums[j]
                if x in want_set:
                    ans = (-want, want-x, x)
                    if ans not in test:
                        rst.append(list(ans))
                        test.add(ans)
                else:
                    want_set.add(want - x)
        return rst

    # after sort
    # can pass many same elems!

if __name__ == '__main__':
    xx = Solution()
    xx.threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])