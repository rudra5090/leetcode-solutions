class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            # New subsequences formed by adding ch
            new = (total + 1) % MOD

            # Replace the old subsequences ending with ch
            total = (total + new - dp[i]) % MOD

            dp[i] = new

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna