class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original_index)
        arr = []
        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        result = [0] * n

        start = 0

        while start < n:
            end = start

            # Find all values belonging to the same group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Collect original indices of this group
            indices = []
            for i in range(start, end + 1):
                indices.append(arr[i][1])

            # Sort original indices
            indices.sort()

            # Values are already sorted
            for i in range(len(indices)):
                result[indices[i]] = arr[start + i][0]

            start = end + 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna