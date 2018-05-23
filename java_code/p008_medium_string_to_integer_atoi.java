// class Solution
class stringToIntegerAtoi {
    // need to handle when str > 2**63-1
    // better to just check over Integer(handle +- boundary)
    public int myAtoi(String str) {
        str = str.trim();
        int len = str.length();
        if (len == 0) return 0;
        boolean negative = false;
        int start = 0;
        if (str.charAt(0) == '-') {
            start = 1;
            negative = true;
        } else if (str.charAt(0) == '+') {
            start = 1;
        }

        long result = 0;
        for (; start < len; start++) {
            char c = str.charAt(start);
            if (c < '0' || c > '9') break;
            long tmp = result * 10 + (c - '0');
            // overflow: not always work, can overflow to positive
//            if (result < 0) {
//                return negative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
//            }
            if (tmp < result) return negative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            else result = tmp;
        }
        if (negative) result = -result;
        if (result > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (result < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        return (int) result;
    }

    public static void main(String[] args) {
        stringToIntegerAtoi a = new stringToIntegerAtoi();
        a.myAtoi("18446744073709551617");
    }
}