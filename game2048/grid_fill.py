import game2048.grid_creation as grc
import random
import os

def grid_to_string(game_grid, n):
    k=" ===" * len(game_grid) + " "
    a=""
    for i in game_grid:
        a+=k+"\n"
        for ij in i:
            a+="| "+str(ij)+" "
        a+="|"+"\n"
    a+=k
    return a

def long_value(game_grid):
    maxlen=1
    for i in game_grid:
        for ij in i:
            if len(str(ij))>maxlen:
                maxlen=len(str(ij))
    return maxlen

def grid_to_string_with_size(game_grid, n):
    maxlong=long_value(game_grid)
    k= (" "+"="*(maxlong+2)) * len(game_grid) + " "
    a=""
    for i in game_grid:
        a+=k+"\n"
        for ij in i:
            d=str(ij)
            a+="| "+d+" "*(maxlong+1-len(d))
        a+="|"+"\n"
    a+=k
    return a

THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def grid_to_string_with_size_and_theme(game_grid,THEME,n):
    k=len(game_grid)
    New_grid=grc.create_grid(k)
    for i in range(0,k):
        for j in range(0,k):
            New_grid[i][j]=THEME[game_grid[i][j]]
    return grid_to_string_with_size(New_grid,n)

def long_value_with_theme(game_grid,THEME):
    k=len(game_grid)
    New_grid=grc.create_grid(k)
    for i in range(0,k):
        for j in range(0,k):
            New_grid[i][j]=THEME[game_grid[i][j]]
    return long_value(New_grid)








