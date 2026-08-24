class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Compute prefix sums in-place or via a prefix array
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Base case: at index n - 1, player must take all stones
        dp = prefix[n - 1]

        # Iterate backwards from n - 2 down to 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna