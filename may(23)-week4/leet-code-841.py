class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque()
        q.append(rooms[0])
        openedroom=set()
        openedroom.add(0)
        while q:
            keys=q.popleft()
            for key in keys:
                if key not in openedroom:
                    q.append(rooms[key])
                    openedroom.add(key)
                
                
        if len(openedroom)==len(rooms):
            return True
        else:
            return False                
               


