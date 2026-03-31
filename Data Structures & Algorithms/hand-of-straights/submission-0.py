class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for x in sorted(count):
            freq = count[x]
            if freq > 0:
                for i in range(groupSize):
                    if count[x + i] < freq:
                        return False
                    count[x + i] -= freq

        return True