import sys 
input = sys.stdin.readline 

while(True):
    tri = list(map(int, input().rstrip().split()))
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    else: 
        tri.sort(reverse=True)
        if tri[0]**2 == tri[1]**2 + tri[2]**2:
            print('right')
        else:
            print('wrong')        
    