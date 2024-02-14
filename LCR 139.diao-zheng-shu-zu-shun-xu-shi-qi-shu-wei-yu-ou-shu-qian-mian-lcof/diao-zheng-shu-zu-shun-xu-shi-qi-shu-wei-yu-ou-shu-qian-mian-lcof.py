class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        left, right = 0, len(actions) - 1
        while left < right:
            if actions[left] & 1 == 1:
                left += 1
            elif actions[right] & 1 == 0:
                right -= 1
            elif actions[left] & 1 == 0 and actions[right] & 1 == 1:
                actions[left], actions[right] = actions[right], actions[left]
                left += 1
                right -= 1
        return actions
