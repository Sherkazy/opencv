import numpy
# scipy.special for the sigmoid function expit()
import scipy.special

# helper to load data from PNG image files
import imageio
# glob helps select multiple files using patterns
import glob
# library for plotting arrays
import matplotlib.pyplot

import cv2
import os
import numpy as np
import csv

text = ''
our_own_dataset = []

csvimg = []
labels = []
for item in range(5):
    if item == 1:
        text = '?'
    elif item == 2:
        text = '??'
    elif item == 3:
        text = '???'
    elif item == 4:
        text = '????'
    else:
        continue
    i = 0
    for image_file_name in glob.glob('../gradient_tabuu/triangle/' + text + '.png'):
        label = 1
        img = cv2.imread(image_file_name, 0)
        csvimg.append(img)
        labels.append(label)
        if i == 1:
            break
        i += 1

        np.savetxt("pixel_data.csv", img)
    # for image_file_name in glob.glob('shapes/triangle/' + text + '.png'):
    #     label = 2
    #     img_array = imageio.imread(image_file_name, as_gray=True)
    #     img_data = 255.0 - img_array.reshape(40000)
    #     record = numpy.append(label, img_data)
    #     our_own_dataset.append(record)
    #     pass
    # for image_file_name in glob.glob('shapes/circle/' + text + '.png'):
    #     label = 0
    #     img_array = imageio.imread(image_file_name, as_gray=True)
    #     img_data = 255.0 - img_array.reshape(40000)
    #     record = numpy.append(label, img_data)
    #     our_own_dataset.append(record)
    #     pass
