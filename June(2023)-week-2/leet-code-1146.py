class SnapshotArray:
 

    def __init__(self, length: int):
        self.arr=[[[0,0]] for _ in range(length)]
        self.ap_id=0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.ap_id,val])

    def snap(self) -> int:
        self.ap_id+=1
        return self.ap_id-1

    def get(self, index: int, snap_id: int) -> int:
        x=bisect.bisect_right(self.arr[index],[snap_id,10**9])
         
        return self.arr[index][x-1][1]

           


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
