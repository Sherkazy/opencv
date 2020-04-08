import cv2 as cv

img = cv.imread('shapes/star/100.png', 0)
laplacian = cv.Laplacian(img, cv.CV_64F)
for i in range(200):
    for j in range(200):
        if laplacian[i][j] < 20:
            laplacian[i][j] = 255
        else:
            laplacian[i][j] = 0

cv.imwrite('gradient_tabuu/colorun_almawtyruu_color_20.jpg', laplacian)
