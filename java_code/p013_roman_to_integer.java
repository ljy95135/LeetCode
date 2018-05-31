import java.util.HashMap;
import java.util.Map;

// Solution
class romanToInteger {
    public int romanToInt(String s) {
        Map<Character, Integer> transMap = new HashMap<>();
        transMap.put('I', 1);
        transMap.put('V', 5);
        transMap.put('X', 10);
        transMap.put('L', 50);
        transMap.put('C', 100);
        transMap.put('D', 500);
        transMap.put('M', 1000);
        int result = 0;
        int previousNum = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int num = transMap.get(s.charAt(i));
            if (num >= previousNum) {
                result += num;
                previousNum = num;
            } else result -= num;

        }
        return result;
    }
}
