import numpy as np
from PIL import Image, ImageDraw

FileFolder = 'my_circle2/'  # Файл для результата
n, m = 100, 100
for k in range(15000):
    ploshad = 0.0
    counter = 0
    check = False
    while ploshad < 0.05 * (n - 2) * (m - 2):
        point = list(np.random.randint(low=1, high=(n + m) / 2, size=2))
        h = np.random.randint(low=1, high=(n + m) / 2, size=1)
        print(point, h, ploshad)
        ploshad = np.abs(h * h)
        if point[0]+h > n or point[1]+h > m:
            ploshad = 0
    img = Image.new("1", (m, n))
    draw = ImageDraw.Draw(img)  # Инструмент сүрөт тартуу үчүн
    draw.ellipse((point[0], point[1], point[0] + h, point[1] + h), width=1, fill=0, outline=1)
    # draw.ellipse((10, 20, 80, 30), width=1, fill=0, outline=1)
    if k < 10:
        img.save(FileFolder + "000" + str(k) + ".png", "PNG")
    elif k < 100:
        img.save(FileFolder + "00" + str(k) + ".png", "PNG")
    elif k < 1000:
        img.save(FileFolder + "0" + str(k) + ".png", "PNG")
    elif k < 15001:
        img.save(FileFolder + str(k) + ".png", "PNG")
    # else:
    #     img.save("my_circle_test/" + str(k) + ".png", "PNG")
    img.close()
