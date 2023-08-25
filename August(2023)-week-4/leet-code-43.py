class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {
        "0":0,    
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        0:'0',
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
        n=len(num1)-1
        m=len(num2)-1
        num1int=0
        num2int=0
        for i in num1:
            num1int+=digit_map[i]*(10**n)
            n-=1
        for j in num2:
            num2int+=digit_map[j]*(10**m)
            m-=1
        ans=num1int*num2int
        res=[]
        if ans<10:
            return digit_map[ans]
            
        while ans>0:
            x=ans%10
            res.append(digit_map[x])
            ans//=10

        return ''.join(res[::-1]) 
