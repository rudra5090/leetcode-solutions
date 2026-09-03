class Solution:
    def findMissingElements(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        result = []

        for i in range(minimum, maximum + 1):
            if i not in nums:
                result.append(i)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna