from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Sort by start time
        arr = sorted(
            [(s, e, w, i) for i, (s, e, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        # dp[i][k] = (maximum weight, selected original indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            s, e, w, original_index = arr[i]

            # Find first interval with start > current end
            nxt = bisect_right(starts, e)

            for k in range(1, 5):

                # Skip current interval
                skip_weight, skip_indices = dp[i + 1][k]

                # Take current interval
                next_weight, next_indices = dp[nxt][k - 1]

                take_weight = w + next_weight

                take_indices = tuple(
                    sorted((original_index,) + next_indices)
                )

                if take_weight > skip_weight:
                    dp[i][k] = (take_weight, take_indices)

                elif take_weight < skip_weight:
                    dp[i][k] = (skip_weight, skip_indices)

                else:
                    # Same weight -> lexicographically smaller indices
                    dp[i][k] = (
                        take_weight,
                        min(take_indices, skip_indices)
                    )

        return list(dp[0][4][1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna