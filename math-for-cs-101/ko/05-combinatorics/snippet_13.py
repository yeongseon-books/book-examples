"""Generated from book-content article."""

def catalan(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = sum(dp[j] * dp[i-1-j] for j in range(i))
    return dp[n]

for i in range(6):
    print(i, catalan(i))
