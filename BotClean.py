# Same code for BotClean Stochastic,BotClean Large

#function
def next_move(posr, posc, board):
    import math
    location_d = list()
    
    for index,row in enumerate(board):
        for col,inrow in enumerate(row):
            if inrow == 'd':
                 location_d.append([index,col])       
    
    bot_pos = [posr,posc]
    
    all_distance = list()
    for i in range(len(location_d)):
        #manhattan distance getting stuck when there is dirty both side
        distance = int(abs(location_d[i][0] - bot_pos[0]) + abs(location_d[i][1] - bot_pos[1]))
        #euclidean distance
        #distance = math.sqrt(((location_d[i][0] - bot_pos[0])**2) + ((location_d[i][1] - bot_pos[1])**2))
        all_distance.append(distance)
    
    
    sortclose_d = [x for (y,x) in sorted(zip(all_distance,location_d))]
    
    if sortclose_d[0][0] < bot_pos[0]:
        print('UP')
    elif sortclose_d[0][0] > bot_pos[0]:
        print('DOWN')
    elif sortclose_d[0][1] > bot_pos[1]:
        print('RIGHT')
    elif sortclose_d[0][1] < bot_pos[1]:
        print('LEFT')
    else:
        print('CLEAN')
            
    


#input
pos = [int(i) for i in input().strip().split()]
board = [[j for j in input().strip()] for i in range(5)]

#function
next_move(pos[0], pos[1], board)
