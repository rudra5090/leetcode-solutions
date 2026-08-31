class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = float('inf')
        first_critical = -1
        last_critical = -1
        
        prev_node = head
        curr_node = head.next
        index = 1
        
        while curr_node and curr_node.next:
            next_node = curr_node.next
            is_critical = (curr_node.val > prev_node.val and curr_node.val > next_node.val) or \
                          (curr_node.val < prev_node.val and curr_node.val < next_node.val)
            
            if is_critical:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                last_critical = index
                
            prev_node = curr_node
            curr_node = next_node
            index += 1
            
        if min_distance == float('inf'):
            return [-1, -1]
            
        return [min_distance, last_critical - first_critical]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna