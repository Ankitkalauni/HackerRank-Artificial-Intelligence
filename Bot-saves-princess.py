def find(grid):
    
    bot = list()
    princess = list()

    for index, row in enumerate(grid):    
        if 'm' in row.lower():
            bot.append((index,row.lower().index('m')))
        if 'p' in row.lower():
            princess.append((index,row.lower().index('p')))
            
    if len(princess)==0 | len(bot)==0:
        print('ERROR\n')
    else:
        indexdis = bot[0][0] - princess[0][0]
        coldis = bot[0][1] - princess[0][1]

        if indexdis > 0:
            for i in range(0,abs(indexdis)):
                print('UP')
        elif indexdis < 0:
            for i in range(0,abs(indexdis)):
                print('Down')   
    
        if coldis > 0:
            for i in range(0,abs(coldis)):
                print('LEFT')
        elif coldis < 0:
            for i in range(0,abs(coldis)):
                print('RIGHT')
        
 

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())


find(grid)
