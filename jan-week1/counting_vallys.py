def countingValleys(steps, path):
    for i in range(steps):
        count=vallycounter=0
        
        values={'D':-1,'U':1}
        
        for step in  path:
            count=count+values[step]
            if count==0 and step=='U':
                vallycounter+=1
        return vallycounter
