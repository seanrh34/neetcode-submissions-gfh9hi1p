class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        LEN = len(s)
        postfix = []
        curDict = defaultdict(int)

        for i in range(LEN - 1, -1, -1):
            curChar = s[i]
            curDict[s[i]] += 1
            postfix = [curDict] + postfix
            
        out = []
        inSub = set()
        counter = 1

        for i in range(LEN):
            curChar = s[i]
            curDict[curChar] -= 1
            inSub.add(curChar)

            startNew = True
            ## inSub chars to the right are no more, break
            for c in inSub:
                if curDict[c] != 0:
                    startNew = False
                    break

            if startNew:
                out.append(counter)
                counter = 1
                inSub = set()
            else:
                counter += 1

        return out