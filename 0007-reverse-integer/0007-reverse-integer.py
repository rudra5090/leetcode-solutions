class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying by 10
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna