"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap={emp.id:emp for emp in employees}
        def dfs(id):
            empl=emap[id]
            return empl.importance+sum(dfs(id) for id in empl.subordinates)
        return dfs(id)
