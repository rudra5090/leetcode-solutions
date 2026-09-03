class Solution:
    def uniformArray(self, nums1):
        min_odd = 10**18
        min_even = 10**18

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # Try to make everything EVEN
        possible = True

        for x in nums1:
            if x % 2 == 1:
                # odd - odd = even
                if min_odd >= x:
                    possible = False
                    break

        if possible:
            return True

        # Try to make everything ODD
        possible = True

        for x in nums1:
            if x % 2 == 0:
                # even - odd = odd
                if min_odd >= x:
                    possible = False
                    break

        if possible:
            return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna