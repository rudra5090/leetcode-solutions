class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        pairs = []

        for i in range(n):
            pairs.append((nums[i], i))

        pairs.sort()
        result = nums[:]
        start = 0

        while start < n:
            end = start
            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            indices = []
            for k in range(start, end + 1):
                indices.append(pairs[k][1])
            indices.sort()

            for k in range(len(indices)):
                result[indices[k]] = pairs[start + k][0]

            start = end + 1

        return result
