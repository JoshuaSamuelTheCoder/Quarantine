/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
*/

#include <limits.h>
#define MIN(A,B) ((A) <= (B)? (A): (B))
int coinChange(int* coins, int coinsSize, int amount){

    int *dp = (int *) calloc(amount+1, sizeof(int));

    //memset(dp, 1, amount+1);
    for(int k = 0; k <= amount; k++) {
        dp[k] = INT_MAX;
    }

    dp[0] = 0;
    //0...amount
    for(int i = 0; i <= amount; i++) {
       for(int j = 0; j < coinsSize; j++) {
           int c = coins[j];
           if (i - c >= 0 && dp[i-c] != INT_MAX) {
               dp[i] = MIN(dp[i], dp[i-c] + 1);
           }
       }
    }

    if (dp[amount] == INT_MAX) {
        return -1;
    }

    return dp[amount];

}
