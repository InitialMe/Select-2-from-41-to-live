def move(man,sep):
    for i in range(sep):
        item = man.pop(0)
        man.append(item)
        
        
def start(player=41,sep=3,rest=2):
    print('总共%d个人，每数到%d淘汰一个人，最后剩下%d个人'%(player,sep,rest))
    
    man = [i for i in range(1,man+1)]
    print('玩家列表：',man)
    sep-=1
    
    while len(player)>rest:
        move(player,sep)
        print('淘汰',player.pop(0))
        
    return player
    
service = start()

print(service)
   
        
    
    
