class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        multiple = k

        while True:
            found = False

            for num in nums:
                if num == multiple:
                    found = True
                    break

            if found == False:
                return multiple

            multiple = multiple + k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna