// Solution
class palindromeNumber {
    public boolean isPalindrome(int x) {
        String xx = String.valueOf(x);
        return xx.equals(new StringBuilder(xx).reverse().toString());
    }
}
