
def move_row_left(L):
    a,b,c,d=L[0],L[1],L[2],L[3]
    if c==0:
        c=d
        d=0
    if b==0:
        b,c=c,d
        d=0
    if a==0:
        a,b,c=b,c,d
        d=0
    if a==b and c==d:
        a+=b
        c+=d
        b,c,d=c,0,0
    elif a==b:
        a+=b
        b,c=c,d
        d=0
    elif b==c:
        b+=c
        c=d
        d=0
    elif c==d:
        c+=d
        d=0
    T=[a,b,c,d]
    return T

def move_row_right(L):
    T=move_row_left(L)
    i=len(T)-1
    while T[i]==0 and len(T)!=0:
        T.pop()
        i=i-1
    T=(len(L)-1-i)*[0]+T
    return T

def move_grid_up(game_grid):
    n=len(game_grid)
    T=[0]*n
    for j in range(0,n):
        for i in range(0,n):
            T[i]=game_grid[i][j]
        T=move_row_left(T)
        for i in range(0,n):
            game_grid[i][j]=T[i]
    return game_grid

def move_grid_down(game_grid):
    n=len(game_grid)
    T=[0]*n
    for j in range(0,n):
        for i in range(0,n):
            T[i]=game_grid[i][j]
        T=move_row_right(T)
        for i in range(0,n):
            game_grid[i][j]=T[i]
    return game_grid

def move_grid_right(game_grid):
    n=len(game_grid)
    for i in range(0,n):
        game_grid[i]=move_row_right(game_grid[i])
    return game_grid

def move_grid_left(game_grid):
    n=len(game_grid)
    for i in range(0,n):
        game_grid[i]=move_row_left(game_grid[i])
    return game_grid

def move_grid(game_grid,command):
    if command== "left" :
        return move_grid_left(game_grid)
    elif command== "right" :
        return move_grid_right(game_grid)
    elif command== "up":
        return move_grid_up(game_grid)
    elif command== "down":
        return move_grid_down(game_grid)

