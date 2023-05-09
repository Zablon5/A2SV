class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx=0
        for num in nums:
            mx=mx|num
        def check(lis):
            oR=0
            for num in lis:
                oR|=num
            if oR==mx:
                return True


        
        combinations = []
        ans=0
        # Generate all possible combinations of length 1 to length of numbers list
        for i in range(1, len(nums) + 1):
            combinations.extend(list(itertools.combinations(nums, i)))
        for comb in combinations:
            if check(comb):
                ans+=1
        return ans        
