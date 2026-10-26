class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_l = [0] * 26
        s2_l = [0] * 26

        for ch in s1:
            s1_l[ord(ch) - ord('a')] += 1

        left = 0
        right = len(s1) - 1

        for i in range(len(s1)):
            s2_l[ord(s2[i]) - ord('a')] += 1

        print(str(s2_l))
        if str(s1_l) == str(s2_l):
            return True

        s2_l[ord(s2[left]) - ord('a')] -= 1
        left += 1
        right += 1

        while right < len(s2):
            s2_l[ord(s2[right]) - ord('a')] += 1
            print(s2_l)

            if str(s1_l) == str(s2_l):
                return True

            s2_l[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1

        return False