import numpy as np
from PIL import Image, ImageDraw

FileFolder = 'RaiymbekAgai/my_triangle2'  # Файл для результата
n, m = 100, 100
for k in range(15000):
    ploshad = 0.0
    while ploshad < 0.005 * (n - 2) * (m - 2):
        point = list(np.random.randint(low=1, high=(n + m) / 2, size=6))
        ploshad = np.abs(
            0.5 * ((point[0] - point[4]) * (point[3] - point[5]) - (point[2] - point[4]) * (point[1] - point[5])))
    point = point + point[0:2]
    img = Image.new("1", (m, n))
    width = img.size[0]  # Туурасын өлчөмүн аныктайбыз
    height = img.size[1]  # Бийиктигинин  өлчөмүн аныктайбыз
    draw = ImageDraw.Draw(img)  # Инструмент сүрөт тартуу үчүн
    draw.line(point, width=1, fill=1)
    if k < 10:
        img.save(FileFolder + "/" + "000" + str(k) + ".png", "PNG")
    elif k < 100:
        img.save(FileFolder + "/" + "00" + str(k) + ".png", "PNG")
    elif k < 1000:
        img.save(FileFolder + "/" + "0" + str(k) + ".png", "PNG")
    elif k < 15001:
        img.save(FileFolder + "/" + str(k) + ".png", "PNG")
    # else:
    #     img.save(FileFolder + "_test/" + str(k) + ".png", "PNG")
    img.close()
