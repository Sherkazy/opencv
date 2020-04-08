import numpy
import imageio
import glob
import cv2 as cv

our_own_dataset = []
text = ''
root_path = '100x100'
scale_percent = 50
middle_color = 100
for item in range(4):
    print(item)
    if item == 0:
        text = '?'
    elif item == 1:
        text = '??'
    elif item == 2:
        text = '???'
    elif item == 3:
        text = '????'
    else:
        continue
    for image_file_name in glob.glob('../shapes/star_test/' + text + '.png'):
        img = cv.imread(image_file_name, 0)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        laplacian = cv.Laplacian(resized, cv.CV_64F)
        for i in range(100):
            for j in range(100):
                if laplacian[i][j] < middle_color:
                    laplacian[i][j] = 0
                else:
                    laplacian[i][j] = 255
        print(image_file_name.split('/')[len(image_file_name.split('/')) - 1])
        cv.imwrite(root_path+'/star_test/' + image_file_name.split('/')[len(image_file_name.split('/')) - 1], laplacian)
    # break

    for image_file_name in glob.glob('../shapes/square_test/' + text + '.png'):
        img = cv.imread(image_file_name, 0)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        laplacian = cv.Laplacian(resized, cv.CV_64F)
        for i in range(100):
            for j in range(100):
                if laplacian[i][j] < middle_color:
                    laplacian[i][j] = 0
                else:
                    laplacian[i][j] = 255
        print(image_file_name.split('/')[len(image_file_name.split('/')) - 1])
        cv.imwrite(root_path+'/square_test/' + image_file_name.split('/')[len(image_file_name.split('/')) - 1], laplacian)

    for image_file_name in glob.glob('../shapes/circle_test/' + text + '.png'):
        img = cv.imread(image_file_name, 0)# percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        laplacian = cv.Laplacian(resized, cv.CV_64F)
        for i in range(100):
            for j in range(100):
                if laplacian[i][j] < middle_color:
                    laplacian[i][j] = 0
                else:
                    laplacian[i][j] = 255
        print(image_file_name.split('/')[len(image_file_name.split('/')) - 1])
        cv.imwrite(root_path+'/circle_test/' + image_file_name.split('/')[len(image_file_name.split('/')) - 1], laplacian)

    for image_file_name in glob.glob('../shapes/triangle_test/' + text + '.png'):
        img = cv.imread(image_file_name, 0)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        laplacian = cv.Laplacian(resized, cv.CV_64F)
        for i in range(100):
            for j in range(100):
                if laplacian[i][j] < middle_color:
                    laplacian[i][j] = 0
                else:
                    laplacian[i][j] = 255
        print(image_file_name.split('/')[len(image_file_name.split('/')) - 1])
        cv.imwrite(root_path+'/triangle_test/' + image_file_name.split('/')[len(image_file_name.split('/')) - 1], laplacian)

print("SUCCESSFULLY FINISH!!!")
