class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        out = ""
        len_out = float("inf")

        tDict = {}
        window = {}
        
        for ch in t:
            tDict[ch] = 1 + tDict.get(ch, 0)

        need = len(tDict)
        have = 0
        left = 0

        for i in range(len(s)):
            curChar = s[i]
            window[curChar] = 1 + window.get(curChar, 0)

            if curChar in tDict and window[curChar] == tDict[curChar]:
                have += 1
            
            while have == need:
                if (i - left + 1) < len_out:
                    out = s[left:i+1]
                    len_out = i - left + 1
                
                window[s[left]] -= 1
                if s[left] in tDict and window[s[left]] < tDict[s[left]]:
                    have -= 1
                left += 1

        if len_out != float("inf"):
            return out
        else:
            return ""
                
        