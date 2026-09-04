class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        for i in range(n):
            left_max = nums[0]

            # Maximum from index 0 to i
            for j in range(1, i + 1):
                if nums[j] > left_max:
                    left_max = nums[j]

            right_min = nums[i]

            # Minimum from index i to n-1
            for j in range(i + 1, n):
                if nums[j] < right_min:
                    right_min = nums[j]

            if left_max - right_min <= k:
                return i

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna