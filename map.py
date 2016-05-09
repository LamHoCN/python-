chart={"A":["B","D"],"C":["E"],"D":["C","E"]}
def path(chart,x,y,pathd=[]):
   
    pathd = pathd +[x]
    print pathd
    if x==y:
        return pathd
    if not chart.has_key(x):
        return None
        
    for jd in chart[x]:
        print 'jd1:',jd
        if jd not in pathd:
            newjd = path(chart,jd,y,pathd)
            print 'jd2:',jd
            
        if newjd:
            return newjd
            



