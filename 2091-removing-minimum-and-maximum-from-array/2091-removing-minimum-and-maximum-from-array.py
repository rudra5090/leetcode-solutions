class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        # Find minimum and maximum values
        min_val = nums[0]
        max_val = nums[0]

        min_pos = 0
        max_pos = 0

        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_pos = i

            if nums[i] > max_val:
                max_val = nums[i]
                max_pos = i

        # Put min_pos before max_pos
        if min_pos > max_pos:
            min_pos, max_pos = max_pos, min_pos

        # 1. Both from front
        front = max_pos + 1

        # 2. Both from back
        back = n - min_pos

        # 3. One from front, one from back
        both = (min_pos + 1) + (n - max_pos)

        return min(front, back, both)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna