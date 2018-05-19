// class Solution
class coinChangeSolution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0 || coins.length == 0) return -1;
        // 0 for not set, -1 for impossible
        int[] result = new int[amount + 1];
        // init coins
        // don't  forget to discard coin larger than amount
        for (int coinValue : coins) {
            if (coinValue <= amount) result[coinValue] = 1;
        }
        for (int i = 1; i < result.length; i++) {
            if (result[i] != 0) continue;
            for (int coinValue : coins) {
                if (i < coinValue || result[i - coinValue] == -1) continue;
                int num = result[i - coinValue] + 1;
                if (result[i] > num || result[i] == 0) result[i] = num;
            }
            if (result[i] == 0) result[i] = -1;
        }

        return result[amount];
    }
}
