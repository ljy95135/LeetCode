import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

// Solution
class threeSumSolution {
    // too slow
    // double pointer for second for-loop will be faster
    // then no neec to check in a Set
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> rst = new ArrayList<>();
        Arrays.sort(nums);
        Set<List<Integer>> answerSet = new HashSet<>();
        for (int i = 0; i < nums.length - 2; i++) {
            int want = -nums[i];
            if (want < 0) break;
            if (i != 0 && nums[i] == nums[i - 1]) continue;

            Set<Integer> wantSet = new HashSet<>();
            for (int j = i + 1; j < nums.length; j++) {
                int x = nums[j];
                if (wantSet.contains(x)) {
                    List<Integer> ans = new ArrayList<>();
                    ans.add(-want);
                    ans.add(want - x);
                    ans.add(x);
                    if (!answerSet.contains(ans)) {
                        answerSet.add(ans);
                        rst.add(ans);
                    }
                } else {
                    wantSet.add(want - x);
                }
            }
        }
        return rst;
    }
}
