class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Try to make the answer greater at position i.
        # Start from the rightmost position because that
        # gives the smallest possible answer.
        for i in range(n - 1, -1, -1):

            remaining = freq[:]

            # Keep target[0:i] exactly the same
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # Find the smallest character greater than target[i]
            current = ord(target[i]) - ord('a')

            for c in range(current + 1, 26):

                if remaining[c] > 0:

                    # Prefix equal to target
                    answer = target[:i]

                    # Make this position greater
                    answer += chr(c + ord('a'))

                    remaining[c] -= 1

                    # Fill remaining characters in sorted order
                    for x in range(26):
                        while remaining[x] > 0:
                            answer += chr(x + ord('a'))
                            remaining[x] -= 1

                    return answer

        return ""

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna