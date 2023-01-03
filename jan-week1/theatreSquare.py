import math

input = input()

slist=input.split()
n=int(slist[0])
m=int(slist[1])
a=int(slist[2])



def theatreSquares(n, m, a):
    if a != 0:
        return (math.ceil(n / a)) * (math.ceil(m / a))


print(theatreSquares(n,m,a))
