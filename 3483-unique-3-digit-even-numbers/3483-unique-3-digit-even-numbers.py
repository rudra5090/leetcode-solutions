class Solution:
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = [a, b, c]
            temp = digits.copy()

            possible = True

            for d in need:
                if d in temp:
                    temp.remove(d)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna