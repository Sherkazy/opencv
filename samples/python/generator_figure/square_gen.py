import numpy as np
from PIL import Image, ImageDraw

n, m = 200, 200
for k in range(1000):
    ploshad = 0.0
    while ploshad < 0.05 * (n - 2) * (m - 2):
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
        img.save("my_square/" + "00" + str(k) + ".png", "PNG")
    elif k < 100:
        img.save("my_square/" + "0" + str(k) + ".png", "PNG")
    else:
        img.save("my_square/" + str(k) + ".png", "PNG")
    img.close()
