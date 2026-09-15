class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        # palindrome[l][r] tells whether s[l:r+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if length == 1:
                    palindrome[l][r] = True
                elif length == 2:
                    palindrome[l][r] = (s[l] == s[r])
                else:
                    palindrome[l][r] = (
                        s[l] == s[r] and palindrome[l + 1][r - 1]
                    )

        # DP
        for r in range(n):
            # Don't select a palindrome ending at r
            dp[r + 1] = dp[r]

            # Try every palindrome ending at r
            for l in range(r + 1):
                length = r - l + 1

                if length >= k and palindrome[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n] 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna