class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        
        def slope(i):
            p1=coordinates[i]
            p2=coordinates[i-1]
            if (p2[0]-p1[0])==0:
                return float(inf)
            slope=(p2[1]-p1[1])/(p2[0]-p1[0])
            return slope
        i=1
        while i<n and slope(i)==slope(i-1):
            i+=1
        if i==n:
            return True
        else:
            return False     
