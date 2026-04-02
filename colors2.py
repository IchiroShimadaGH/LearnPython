import pygame
import random

# 初期設定
rows, cols = 4, 3
cell_size = 100

pygame.init()
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()

# 初期状態（ランダム色）
grid = [
    [ [random.randint(0,255) for _ in range(3)] for _ in range(cols)]
    for _ in range(rows)
]

def next_grid(grid):
    new_grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            # 近傍の平均色に少しランダムを足す
            neighbors = []

            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbors.append(grid[nr][nc])

            avg = [
                sum(n[i] for n in neighbors)//len(neighbors)
                for i in range(3)
            ]

            # 少しランダムに揺らす
            new_color = [
                min(255, max(0, avg[i] + random.randint(-20,20)))
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

    # 1秒ごとに更新
    timer += clock.get_time()
    if timer > 1000:
        grid = next_grid(grid)
        timer = 0

    # 描画
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