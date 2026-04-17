import pygame
import random

# 初期設定
rows, cols = 100, 150
cell_size = 7
th =40
while True:
    try:
        th = int(input("閾値: "))
        if th>=0 and th<=255:
            break
        else:
            print("0以上255以下の整数を入力してください")
        break
    except ValueError:
        print("0以上255以下の整数を入力してください")

noiseproba=1
while True:
    try:
        noiseproba = int(input("noiseproba の確率を百分率で: "))
        if noiseproba>=0 and noiseproba<=100:
            break
        else:
            print("0以上100以下の整数を入力してください")
        break
    except ValueError:
        print("0以上100以下の整数を入力してください")

noise=1
while True:
    try:
        noise = int(input("noiseの値: "))
        if noise>=0 and noise<=10:
            break
        else:
            print("0以上10以下の整数を入力してください")
        break
    except ValueError:
        print("0以上10以下の整数を入力してください")
timeunit=30
dist=1
maxormin=3
while True:
    try:
        maxormin = int(input("maxorminの値: "))
        if maxormin>=1 and maxormin<=10:
            break
        else:
            print("1以上10以下の整数を入力してください")
        break
    except ValueError:
        print("1以上10以下の整数を入力してください")

print("終了するには q を押してください")

pygame.init()
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()

# 初期状態（ランダム色）
grid = [
    [ [random.randint(0,255) for _ in range(3)] for _ in range(cols)]
    for _ in range(rows)
]
# grid = [
#      [ [100,100,100] for _ in range(cols)]
#      for _ in range(rows)
#  ]

def mate(rgb1, rgb2):
    diff=[abs(a- b) for a, b in zip(rgb1, rgb2)]
    if max(diff)>=th:
        return(-1)
    else:
        newrgb=[];
        for a, b in zip(rgb1, rgb2):
            rr=random.randint(0,maxormin-1)
            if rr==0:
                newrgb.append(max(a,b))
            else:
                newrgb.append(min(a,b))
        return(newrgb)

def addnoise(aa):
    rr=random.randint(1,100)
    if rr<=noiseproba:
        xx=random.choice([i for i in range(-noise, noise+1) if i != 0])
        bb=aa+xx
        return(min(255, max(0, bb)))
    else:
        return(aa)
    
    

    

def nextgrid(grid):
    new_grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            if grid[r][c]==-1:
                nn=2
            else:
                nn=1
            
            neighbors = []
            for dr in range(-dist, dist+1):
                nr = (r+dr) % rows
                for dc in range(-dist, dist+1):
                    nc = (c+dc) % cols
                    if grid[nr][nc]!=-1:
                        neighbors.append([nr, nc])
            
            if len(neighbors)>=nn:
                parents=random.sample(neighbors,k=nn)
                if nn==1:
                    parents.append([r, c])

                rgb1=grid[parents[0][0]][parents[0][1]]
                rgb2=grid[parents[1][0]][parents[1][1]]
                newrgb=mate(rgb1, rgb2)

                if newrgb!=-1:
                    newrgb2 = []
                    for i in range(3):
                        newrgb2.append(addnoise(newrgb[i]))
                else:
                    newrgb2 = -1
            else:
                newrgb2=-1


            

            

            row.append(newrgb2)
        new_grid.append(row)

    return new_grid


running = True
timer = 0
timer2 = 0
numb=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    timer += clock.get_time()
    if timer > timeunit:
        grid = nextgrid(grid)
        timer = 0
    timer2 += clock.get_time()
    if timer2 > 1000:
        print(numb)
        timer2 = 0


    numb=0
    for r in range(rows):
        for c in range(cols):
            
            if grid[r][c]==-1:
                color=[0,0,0]
                numb=numb+1
                if grid[r][c]!=-1:
                    print("wrong")
            else:
                color = grid[r][c]
            pygame.draw.rect(
                screen,
                color,
                (c*cell_size, r*cell_size, cell_size, cell_size)
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()