// class Solution
class zigZagConversion {
    public String convert(String s, int numRows) {
        if (numRows < 2) return s;

        StringBuilder[] result = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            result[i] = new StringBuilder();
        }
        int count = 0;
        boolean up_state = true;
        int len = s.length();
        for (int i = 0; i < len; i++) {
            if (up_state) {
                result[count++].append(s.charAt(i));
                if (count >= numRows) {
                    up_state = false;
                    count--;
                }
            } else {
                result[--count].append(s.charAt(i));
                if (count == 0) {
                    up_state = true;
                    count = 1;
                }
            }
        }
        StringBuilder r = new StringBuilder();
        for (StringBuilder sb : result) {
            r.append(sb);
        }
        return r.toString();
    }

    public static void main(String[] args) {
        zigZagConversion z = new zigZagConversion();
        System.out.println("Test");
        System.out.println(z.convert("01210", 3));
    }
}