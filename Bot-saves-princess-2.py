def nextMove(n,r,c,grid):
    
    bot = [[r,c]]
    princess = list()
    
    for i,x in enumerate(grid):
        if 'p' in x:
            princess.append([i,x.index('p')])
    
    
    if len(princess)==0 | len(bot)==0:
        print('ERROR\n')
    else:
        indexdis = bot[0][0] - princess[0][0]
        coldis = bot[0][1] - princess[0][1]
    
    if abs(indexdis) > abs(coldis):
        if indexdis!=0:
            if indexdis < 0:
                print('DOWN\n')
            elif indexdis > 0:
                print('UP\n')
        else:
            pass
        
    elif abs(indexdis) < abs(coldis):
        if coldis!=0:
            if coldis < 0:
                print('RIGHT\n')
            elif coldis > 0:
                print('LEFT\n')       
        else:
            pass
    else:
        if indexdis!=0:
            if indexdis < 0:
                print('DOWN\n')
            elif indexdis > 0:
                print('UP\n')
        else:
            pass   

        
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(n,r,c,grid)
