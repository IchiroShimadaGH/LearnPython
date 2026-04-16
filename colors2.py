import pygame
import random

# 初期設定
rows, cols = 100, 150
cell_size = 7
th =50
noise=0 
timeunit=100
dist=2
maxormin=2

pygame.init()
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()

# 初期状態（ランダム色）
grid = [
    [ [random.randint(0,255) for _ in range(3)] for _ in range(cols)]
    for _ in range(rows)
]

def mate(rgb1, rgb2):
    diff=[abs(a- b) for a, b in zip(rgb1, rgb2)]
    if max(diff)>=th:
        return([0,0,0])
    else:
        newrgb=[];
        for a, b in zip(rgb1, rgb2):
            rr=random.randint(0,maxormin-1)
            if rr==0:
                newrgb.append(min(a,b))
            else:
                newrgb.append(max(a,b))
        return(newrgb)

def next_grid(grid):
    new_grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            if grid[r][c]==[0,0,0]:
                nn=2
            else:
                nn=1
            
            neighbors = []
            for dr in range(-dist, dist+1):
                nr = r+dr 
                for dc in range(-dist, dist+1):
                    nc = c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (dr!=0 or dc!=0):
                        if grid[nr][nc]!=[0,0,0]:
                            neighbors.append([nr, nc])
            
            if len(neighbors)>=nn:
                parents=random.sample(neighbors, nn)
                if nn==1:
                    parents.append([r, c])
            
            # print(parents)
            # print(parents[1])
            # print(len(parents[1]))
            # print(parents[1][1], parents[1][2])
            # print(len(grid), len(grid[0]))

            rgb1=grid[parents[0][0]][parents[0][1]]
            rgb2=grid[parents[1][0]][parents[1][1]]
            newrgd=mate(rgb1, rgb2)

            new_color = [
                min(255, max(0, newrgd[i] + random.randint(-3,3)))
                for i in range(3)
            ]

            row.append(new_color)
        new_grid.append(row)

    return new_grid


running = True
timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += clock.get_time()
    if timer > timeunit:
        grid = next_grid(grid)
        timer = 0

    for r in range(rows):
        for c in range(cols):
            color = grid[r][c]
            pygame.draw.rect(
                screen,
                color,
                (c*cell_size, r*cell_size, cell_size, cell_size)
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()