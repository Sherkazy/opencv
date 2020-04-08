# Программа для построение выпуклых замкнутых ломанных разной конфигурации
import numpy as np
from PIL import Image, ImageDraw
import MyFunction as MyF


NumberOfFigures = 15000  # количество фигур
n, m = 100, 100  # Размеры изображении
NumberOfCorners = 4  # Количество вершин
FileFolder = 'my_convex4_2'  # Файл для результата
l0, l1, l2 = 2, int(0.25 * n), int(0.5 * n)
dAngle = 360.0 / NumberOfCorners
clarity = 0.02  # Параметр четкости фигур
file = open(FileFolder + "/test.txt", "w")
file.write("Number of figures=" + str(NumberOfFigures) + " n=" + str(n) +
           " m=" + str(m) + " Number of Corners=" + str(NumberOfCorners) + "\n" +
           "Pixels(n*m)=" + str(n * m) + " Сlarity=" + str(clarity) + " Clarity*n*m>" + str(clarity * n * m) +
           " np.sqrt(Clarity*n*m)>" + str(np.sqrt(clarity * n * m)) + "\n")
for k in range(1, NumberOfFigures + 1):
    measureOfArea, minLong, convex = 0.0, 0.0, True  # Качество фигуры определяем по длине сторон и площади треугольников
    while convex or (measureOfArea < clarity * n * m or minLong < np.sqrt(clarity * n * m)):
        pointX = []
        pointY = []
        for l in range(NumberOfCorners):
            x, y = MyF.PolarRandom1(m, n, l * dAngle, (l + 1) * dAngle, l0, l2 - 1)
            pointX = pointX + [x]
            pointY = pointY + [y]
        measureOfArea = n * m
        minLong = (n + m) / 2.0
        convex = False
        for l in range(NumberOfCorners):  # Площадь треугольника
            measureOfAreaC = (pointX[np.mod(l, NumberOfCorners)] - pointX[np.mod(2 + l, NumberOfCorners)]) * \
                             (pointY[np.mod(1 + l, NumberOfCorners)] - pointY[np.mod(2 + l, NumberOfCorners)]) - \
                             (pointY[np.mod(l, NumberOfCorners)] - pointY[np.mod(2 + l, NumberOfCorners)]) * \
                             (pointX[np.mod(1 + l, NumberOfCorners)] - pointX[np.mod(2 + l, NumberOfCorners)])
            if l == 0:
                znak = measureOfAreaC  # Ореинтация первого треугольника
            if measureOfAreaC * znak < 0.0:
                convex = True
                break
            measureOfAreaC = 0.5 * np.abs(measureOfAreaC)
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
    if k < 10:
        img.save(FileFolder + "/" + "000" + str(k) + ".png", "PNG")
    elif k < 100:
        img.save(FileFolder + "/" + "00" + str(k) + ".png", "PNG")
    elif k < 1000:
        img.save(FileFolder + "/" + "0" + str(k) + ".png", "PNG")
    elif k < 16000:
        img.save(FileFolder + "/" + str(k) + ".png", "PNG")
    else:
        img.save(FileFolder + "_test/" + str(k) + ".png", "PNG")
    img.close()
file.close()
