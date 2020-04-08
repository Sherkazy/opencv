# Программа для построение звездочки разной конфигурации
import MyFunction as MyF
import numpy as np
from PIL import Image, ImageDraw

NumberOfFigures = 10  # количество фигур
n, m = 100, 100  # Размеры изображении
NumberOfCorners = 10  # Количество вершин
FileFolder = 'my_star5_3'  # Файл для результата
l0, l1, l2 = 2, int(0.25 * n), int(0.5 * n)
dAngle = 360.0 / NumberOfCorners
clarity = 0.1  # Параметр четкости фигур
file = open(FileFolder + "/test.txt", "w")
file.write("Number of figures=" + str(NumberOfFigures) + " n=" + str(n) +
           " m=" + str(m) + " Number of Corners=" + str(NumberOfCorners) + "\n" +
           "Pixels(n*m)=" + str(n * m) + " Сlarity=" + str(clarity) + " Clarity*n*m>" + str(clarity * n * m) +
           " np.sqrt(Clarity*n*m)>" + str(np.sqrt(clarity * n * m)) + "\n")
for k in range(1, NumberOfFigures + 1):
    measureOfArea, minLong = 0.0, 0.0  # Качество фигуры определяем по длине сторон и площади треугольников
    while measureOfArea < clarity * n * m or minLong < np.sqrt(clarity * n * m):
        pointX = []
        pointY = []
        switch = True
        for l in range(NumberOfCorners):
            if switch:
                x, y = MyF.PolarRandom1(m, n, l * dAngle, (l + 1) * dAngle, l0, l1 - 1)
            else:
                x, y = MyF.PolarRandom1(m, n, l * dAngle, (l + 1) * dAngle, l1 + 1, l2 - 1)
            switch = not switch
            pointX = pointX + [x]
            pointY = pointY + [y]
        measureOfArea = n * m
        minLong = (n + m) / 2.0
        for l in range(NumberOfCorners):  # Площадь треугольника
            measureOfAreaC = 0.5 * np.abs(
                (pointX[np.mod(l, NumberOfCorners)] - pointX[np.mod(2 + l, NumberOfCorners)]) *
                (pointY[np.mod(1 + l, NumberOfCorners)] - pointY[np.mod(2 + l, NumberOfCorners)]) -
                (pointY[np.mod(l, NumberOfCorners)] - pointY[np.mod(2 + l, NumberOfCorners)]) *
                (pointX[np.mod(1 + l, NumberOfCorners)] - pointX[np.mod(2 + l, NumberOfCorners)]))
            if measureOfArea > measureOfAreaC:
                measureOfArea = measureOfAreaC
        for l in range(NumberOfCorners):  # Длина сторон
            minLongC = np.sqrt((pointX[np.mod(l, NumberOfCorners)] - pointX[np.mod(1 + l, NumberOfCorners)]) ** 2 +
                               (pointY[np.mod(l, NumberOfCorners)] - pointY[np.mod(1 + l, NumberOfCorners)]) ** 2)
            if minLong > minLongC:
                minLong = minLongC
    point = list()
    for l in range(NumberOfCorners):
        point = point + list([pointX[l]]) + list([pointY[l]])
    point = point + point[0:2]
    file.write(str(k) + " " + str(point) + " " + str(round(measureOfArea, 2)) + " " + str(round(minLong, 2)) + "\n")
    img = Image.new("1", (m, n))
    draw = ImageDraw.Draw(img)  # Инструмент сүрөт тартуу үчүн
    draw.line(point, width=1, fill=1)
    # if k < 10:
    #     img.save("C:\\Users\\usr\\Desktop\\Шергазы\\" + FileFolder + "\\" + "00" + str(k) + ".bmp", "bmp")
    # elif k < 100:
    #     img.save("C:\\Users\\usr\\Desktop\\Шергазы\\" + FileFolder + "\\" + "0" + str(k) + ".bmp", "bmp")
    # else:
    #     img.save("C:\\Users\\usr\\Desktop\\Шергазы\\" + FileFolder + "\\" + str(k) + ".bmp", "bmp")

    if k < 10:
        img.save(FileFolder + "/" + "000" + str(k) + ".png", "PNG")
    elif k < 100:
        img.save(FileFolder + "/" + "00" + str(k) + ".png", "PNG")
    elif k < 1000:
        img.save(FileFolder + "/" + "0" + str(k) + ".png", "PNG")
    elif k < 15001:
        img.save(FileFolder + "/" + str(k) + ".png", "PNG")
    else:
        img.save(FileFolder + "_test/" + str(k) + ".png", "PNG")
    img.close()
file.close()
