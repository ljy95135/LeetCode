class Solution:
    # not pass
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     from itertools import combinations
    #     max_area = 0
    #     for c in combinations(enumerate(height), 2):  # combination have sort
    #         max_area = max((c[1][0] - c[0][0]) * min(c[0][1], c[1][1]), max_area)
    #     return max_area
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    x = Solution()
    print(x.maxArea([2, 1]))
