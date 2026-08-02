class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordMap = {}

        def canTransform(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                
                if diff > 1:
                    return False
            
            return True

        wordMap[beginWord] = []
        for w in wordList:
            if canTransform(beginWord, w):
                wordMap[beginWord].append(w)

        for w1 in wordList:
            wordMap[w1] = []
            for w2 in wordList:
                if w1 != w2:
                    if canTransform(w1, w2):
                        wordMap[w1].append(w2)

        print(wordMap)
        visited = set()
        def bfs(curWord, prevWord):
            q = deque()
            q.append([curWord, 1])
            output = 0

            while q:
                curWord, depth = q.popleft()
                print(curWord, depth)

                if curWord in visited:
                    continue

                if curWord == endWord:
                    output = depth

                visited.add(curWord)
                for w in wordMap[curWord]:
                    if w != prevWord:
                        q.append([w, depth + 1])

            return output

        return bfs(beginWord, "")