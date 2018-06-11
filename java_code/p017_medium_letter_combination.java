import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

// Solution
class letterCombination {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.equals("")) return result;
        HashMap<Character, String> num2Letters = new HashMap<>();
        num2Letters.put('2', "abc");
        num2Letters.put('3', "def");
        num2Letters.put('4', "ghi");
        num2Letters.put('5', "jkl");
        num2Letters.put('6', "mno");
        num2Letters.put('7', "pqrs");
        num2Letters.put('8', "tuv");
        num2Letters.put('9', "wxyz");

        // init list
        String letters = num2Letters.get(digits.charAt(0));
        for (int i = 0; i < letters.length(); i++) {
            result.add(String.valueOf(letters.charAt(i)));
        }
        // loop combinations
        for (int i = 1; i < digits.length(); i++) {
            int size = result.size();
            List<String> tmp = new ArrayList<>();
            String nextLetters = num2Letters.get((digits.charAt(i)));
            for (int j = 0; j < size; j++) {
                String x = result.get(j);
                for (int k = 0; k < nextLetters.length(); k++) {
                    tmp.add(x + nextLetters.charAt(k));
                }
            }
            result = tmp;
        }
        return result;
    }

    public static void main(String[] args) {

    }
}
