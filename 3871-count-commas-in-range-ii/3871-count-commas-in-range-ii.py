class Solution:
    def countCommas(self, n):
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1

            if n < end:
                end = n

            count = end - start + 1

            ans += count * commas

            start = start * 1000
            commas += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna