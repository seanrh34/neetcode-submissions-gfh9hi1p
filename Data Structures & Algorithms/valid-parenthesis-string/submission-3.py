class Solution:
    def checkValidString(self, s: str) -> bool:
        left = deque()
        star = deque()
        
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)

            if s[i] == '*':
                star.append(i)

            if s[i] == ')':
                if len(left):
                    left.pop()
                elif len(star):
                    star.pop()
                else:
                    return False

        while len(left) > 0 and len(star):
            if left.pop() > star.pop():
                return False

        return len(left) == 0