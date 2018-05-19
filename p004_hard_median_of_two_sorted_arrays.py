# need be O(log (m+n))
# make two part same len (or p1 = p2+1) at first
# assume m<n and no empty list
# carefully check boundary!
# but seems sort is faster

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        imin = 0
        imax = m
        while True:
            i = (imin + imax) // 2
            # for i[0,m] -> j>=0 and j<=n
            j = (m + n + 1) // 2 - i
            if (i <= 0 or j >= n or nums1[i - 1] <= nums2[j]) and \
                    (j <= 0 or i >= m or nums2[j - 1] <= nums1[i]):
                # for even
                if (m + n) % 2 == 0:
                    if i <= 0:
                        x1 = nums2[j - 1]
                    elif j <= 0:
                        x1 = nums1[i - 1]
                    else:
                        x1 = max(nums2[j - 1], nums1[i - 1])
                    if i >= m:
                        x2 = nums2[j]
                    elif j >= n:
                        x2 = nums1[i]
                    else:
                        x2 = min(nums1[i], nums2[j])
                    return (x1 + x2) / 2
                # for odd
                if i <= 0:
                    return nums2[j - 1]
                if j <= 0:
                    return nums1[i - 1]
                return max(nums2[j - 1], nums1[i - 1])
            if j > 0 and i < m and nums2[j - 1] > nums1[i]:  # increase i
                imin = i + 1
            else:
                imax = i - 1
