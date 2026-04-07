from PIL import Image, ImageDraw
import random

cell_size = 50
cols, rows = 6, 8

img = Image.new("RGB", (cols * cell_size, rows * cell_size))
draw = ImageDraw.Draw(img)

for i in range(cols):
    for j in range(rows):
        color = tuple(random.randint(0, 255) for _ in range(3))
        x0 = i * cell_size
        y0 = j * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        draw.rectangle([x0, y0, x1, y1], fill=color)

img.save("grid.png")