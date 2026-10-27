class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def countHours(k):
            total_hours = 0
            
            for p in piles:
                total_hours += math.ceil(p/k)

            return total_hours

        output = max(piles)

        left = 1
        right = output
        while left <= right:
            mid = (left + right) // 2

            if countHours(mid) <= h:
                output = min(mid, output)
                right = mid - 1
            else:
                left = mid + 1

        return output            
