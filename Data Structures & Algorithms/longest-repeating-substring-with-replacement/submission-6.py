class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        s_dict = defaultdict(int)

        left = 0
        curMax = 0
        maxChar = ''

        for i in range(0, len(s)):
            curC = s[i]
            s_dict[curC] += 1
            
            if s_dict[curC] > curMax:
                curMax = s_dict[curC]
                maxChar = curC

            if (curMax + k) < (i - left + 1):
                s_dict[s[left]] -= 1
                left += 1

            output = max(output, (i - left + 1))

        return output