// Solution

import java.util.Arrays;

class ThreeSumClosestSolutin {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        int diffference = Math.abs(result - target);
        if (diffference == 0) return target;

        for (int i = 0; i < nums.length; i++) {
            int tar = target - nums[i];
            int low = i + 1;
            int high = nums.length - 1;
            while (low < high) {
                int twoSum = nums[low] + nums[high];
                int dif = twoSum - tar;

                if (dif == 0) return target;
                if (dif > 0) high--;
                else low++;

                dif = Math.abs(dif);
                if (dif < diffference) {
                    diffference = dif;
                    result = nums[i] + twoSum;
                }
            }
        }
        return result;
    }
}
