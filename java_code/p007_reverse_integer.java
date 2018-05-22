class reverseInteger {
    // -2147483648=<x<= 2147483647
    public int reverse(int x) {
        if (x == -2147483648) return 0;
        int result;
        boolean negativeFlag = false;
        if (x < 0) {
            x = -x;  // not always works! have to handle -2147483648
            negativeFlag = true;
        }
        StringBuilder str = new StringBuilder(Integer.toString(x));
        long xx = Long.parseLong(str.reverse().toString());
        if (xx > 2147483647 || xx < -2147483648) return 0;
        return (int) (negativeFlag ? -xx : xx);
    }

    public static void main(String[] args) {

        int test = -2147483648;


        String x = "-12";
        String y = "0012";
        String z = "2147483647"; // 2**31-1
        String over = "2147483648";
//        long a = 2147483648; // can't
        long a = (long) Math.pow(2, 31);  // 2147483648
        System.out.println(Integer.parseInt(x));
        System.out.println(Integer.parseInt(y));  // can work with 0012
        System.out.println(Integer.parseInt(z));
//        System.out.println(Integer.parseInt(over)); // NumberFormatException
        System.out.println(Long.parseLong(over));


        System.out.println((int) a);  // overflow not error
        System.out.println((int) (a - 1));
    }
}
