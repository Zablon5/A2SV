class Solution:
    def countSeniors(self, details: List[str]) -> int:
        number_of_elders = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                number_of_elders += 1
        return number_of_elders

            

        