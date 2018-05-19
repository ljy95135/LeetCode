import java.util.HashMap;
import java.util.Map;

// class Solution
// using Array will be even faster (2x)
class longestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int maxResult = 0;
        int currResult = 0;
        int start = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!map.containsKey(c) || map.get(c) < start) {
                currResult++;
                maxResult = Math.max(currResult, maxResult);
            } else {
                start = map.get(c) + 1;
                currResult = i - start + 1;
            }
            map.put(c, i);
        }
        return maxResult;
    }
}
