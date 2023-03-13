class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
            n = len(tickets)
            time = 0
            line = list(range(n))
            
            while True:
                curr_person = line.pop(0)
                tickets[curr_person] -= 1
                if curr_person == k and tickets[curr_person] == 0:
                    return time + 1
                if tickets[curr_person] > 0:
                    line.append(curr_person)
                time += 1
            return time    
