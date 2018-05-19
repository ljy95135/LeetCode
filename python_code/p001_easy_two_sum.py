class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # {the_number_we_need : original_index}
        # O(n)
        d = dict()
        for index, value in enumerate(nums):
            if value in d:
                return [d[value], index]
            d[target - value] = index
