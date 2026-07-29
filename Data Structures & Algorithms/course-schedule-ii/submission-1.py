from typing import List

class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:
        lst = [[] for _ in range(numCourses)]
        output = []

        for course, prereq in prerequisites:
            lst[course].append(prereq)

        visiting = set()
        completed = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in completed:
                return True

            visiting.add(course)

            for prereq in lst[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            completed.add(course)

            # Append only after all prerequisites are added.
            output.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output