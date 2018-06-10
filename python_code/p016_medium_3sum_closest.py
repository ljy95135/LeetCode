class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        difference = abs(result - target)
        if difference == 0: return target

        for i, n in enumerate(nums):
            tar = target - n
            low = i + 1
            high = length - 1
            while low < high:
                two_sum = nums[low] + nums[high]
                if two_sum == tar:
                    return target
                dif = two_sum - tar
                abs_dif = abs(dif)
                if abs_dif < difference:
                    difference = abs_dif
                    result = n + two_sum
                if dif > 0:
                    high -= 1
                else:
                    low += 1

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.threeSumClosest([-1, 2, 1, -4], 1))
    print(x.threeSumClosest([0, 2, 1, -3], 1))
