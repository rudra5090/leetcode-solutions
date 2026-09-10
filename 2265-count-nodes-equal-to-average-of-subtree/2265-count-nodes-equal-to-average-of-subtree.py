class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if node is None:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Floor division gives the required rounded-down average
            average = total_sum // total_count

            if node.val == average:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna