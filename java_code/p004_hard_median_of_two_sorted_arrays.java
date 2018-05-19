// class Solution
// assume no empty list

// another possible way is every time moves forward min(len1, k/2) and k is the number of elems we need to throw
class medianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }
        int m = nums1.length;
        int n = nums2.length;
        int imin = 0;
        int imax = m;
        while (true) {
            // i: [0, m]
            int i = (imin + imax) / 2;
            // j: [0, n]
            int j = (m + n + 1) / 2 - i;
            if ((i <= 0 || j >= n || nums1[i - 1] <= nums2[j]) &&
                    (j <= 0 || i >= m || nums2[j - 1] <= nums1[i])) {
                // for even
                if ((m + n) % 2 == 0) {
                    int x1, x2;
                    if (i <= 0) {
                        x1 = nums2[j - 1];
                    } else if (j <= 0) {
                        x1 = nums1[i - 1];
                    } else {
                        x1 = Math.max(nums2[j - 1], nums1[i - 1]);
                    }
                    if (i >= m) {
                        x2 = nums2[j];
                    } else if (j >= n) {
                        x2 = nums1[i];
                    } else {
                        x2 = Math.min(nums2[j], nums1[i]);
                    }
                    return (x1 + x2) / 2.0;
                }
                // for odd
                if (i <= 0) {
                    return nums2[j - 1];
                }
                if (j <= 0) {
                    return nums1[i - 1];
                }
                return Math.max(nums2[j - 1], nums1[i - 1]);
            }
            if (j > 0 && i < m && nums2[j - 1] > nums1[i]) {
                // increase i
                imin = i + 1;
            } else {
                imax = i - 1;
            }
        }
    }
}
