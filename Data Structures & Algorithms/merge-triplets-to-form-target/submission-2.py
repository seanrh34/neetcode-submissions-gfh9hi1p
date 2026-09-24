class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = triplets[0]

        for t1, t2, t3 in triplets:
            if t1 <= target[0]:
                if t2 <= target[1]:
                    if t3 <= target[2]:
                        cur = [t1, t2, t3]

        if cur == target:
            return True
        
        triplets.sort()
        for i in range(0, len(triplets)):
            nxt = triplets[i]
            if max(cur[0], nxt[0]) <= target[0]:
                if max(cur[1], nxt[1]) <= target[1]:
                    if max(cur[2], nxt[2]) <= target[2]:
                        cur = [max(cur[0], nxt[0]), max(cur[1], nxt[1]), max(cur[2], nxt[2])]
            
            if cur == target:
                return True

        return False