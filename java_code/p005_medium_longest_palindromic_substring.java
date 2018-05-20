class longestPalindromicSubstring {
    public String longestPalindrome(String s) {
        int N = s.length();
        if (N == 0) return "";
        int[][] dp = new int[N][N];
        int maxRow = 0;
        int maxCol = 0;
        int maxResult = 1;
        for (int i = 0; i < N; i++) {
            dp[i][i] = 1;
        }
        for (int i = 0; i < N - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                maxResult = dp[i][i + 1] = 2;
                maxRow = i;
                maxCol = i + 1;
            }
        }
        for (int internal = 2; internal < N; internal++) {
            for (int i = 0; i < N - internal; i++) {
                int j = i + internal;
                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1] != 0) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                    if (dp[i][j] > maxResult) {
                        maxResult = dp[i][j];
                        maxRow = i;
                        maxCol = j;
                    }
                }
            }
        }
        return s.substring(maxRow, maxCol + 1);
    }
}
