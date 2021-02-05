"""
Maximize profit of a certain rod length given prices of smaller rods

Input:
5
1 = $2
2 = $3
3 = $1
4 = $5
5 = $4
"""
def cut_rod(n, costs):
    dp = [0]*(n+1)

    for i in range(1,n+1):
        for c,v in costs.items():
            if i >= c:
                dp[i] = max(dp[i], dp[i - c] + v)
    print(dp)
    return dp[-1]


if __name__ == "__main__":

    rod_length = 5
    prices = {
        1: 2,
        2: 6,
        3: 1,
        4: 5,
        5: 4,
    }
    print(cut_rod(rod_length, prices))
