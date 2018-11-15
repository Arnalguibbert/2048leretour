from math import *
import random
import os


def create_grid(n):
    game_grid = []
    for i in range(0,n):
        game_grid.append([' ' for j in range(0,n)])
    return game_grid


def grid_add_new_tile_at_position(game_grid,i,j):
    game_grid[i][j]=2
    return game_grid

def get_all_tiles(game_grid):
    t=[]
    for i in game_grid:
        for ij in i:
            if ij==' ':
                t.append(0)
            else :
                t.append(ij)
    return t

def get_value_new_tile():
    nombre_aleatoire=random.uniform(0,1)
    if nombre_aleatoire>0.1:
        return 2
    else:
        return 4

def get_empty_tiles_positions(game_grid):
    cases_vides=[]
    n=len(game_grid)
    for i in range(0,n):
        for j in range(0,n):
            if game_grid[i][j]==0 or game_grid[i][j]==' ':
                cases_vides.append((i,j))
    return cases_vides

def get_new_position(game_grid):
    t=get_empty_tiles_positions(game_grid)
    n=len(t)
    nombre_aleatoire=random.randint(0,n-1)
    return t[nombre_aleatoire]

def grid_get_value(game_grid,x,y):
    if game_grid[x][y]==' ':
        game_grid[x][y]=0
    return game_grid[x][y]

def grid_add_new_tile(game_grid):
    i,j=get_new_position(game_grid)
    game_grid[i][j]=get_value_new_tile()
    return game_grid

def init_game(n):
    game_grid=create_grid(n)
    game_grid=grid_add_new_tile(game_grid)
    game_grid=grid_add_new_tile(game_grid)
    return game_grid















