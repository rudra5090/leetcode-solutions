class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        min_pos = 0
        max_pos = 0

        for i in range(1, n):
            if nums[i] < nums[min_pos]:
                min_pos = i
            if nums[i] > nums[max_pos]:
                max_pos = i

        if min_pos > max_pos:
            min_pos, max_pos = max_pos, min_pos

        from_front = max_pos + 1
        from_back = n - min_pos
        one_each = (min_pos + 1) + (n - max_pos)

        return min(from_front, from_back, one_each)
