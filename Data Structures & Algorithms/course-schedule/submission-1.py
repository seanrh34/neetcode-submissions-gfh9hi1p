from collections import deque
from typing import List

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        lst = [[] for _ in range(numCourses)]

        for curCourse, preReq in prerequisites:
            lst[curCourse].append(preReq)

        completed = set()

        for i in range(numCourses):
            if i in completed:
                continue

            # False means enter the node.
            # True means finish processing the node.
            stack = [(i, False)]
            visiting = set()

            while stack:
                curCourse, finished = stack.pop()

                if finished:
                    visiting.remove(curCourse)
                    completed.add(curCourse)
                    continue

                if curCourse in completed:
                    continue

                if curCourse in visiting:
                    return False

                visiting.add(curCourse)

                # Add a finishing step after all prerequisites.
                stack.append((curCourse, True))

                for prereq in lst[curCourse]:
                    if prereq in visiting:
                        return False

                    if prereq not in completed:
                        stack.append((prereq, False))

        return True