import os
from random import shuffle

import numpy as np
import cv2
import os



def loadImages(path, figure):
    '''Put files into lists and return them as one list with all images
     in the folder'''
    image_files = sorted([os.path.join(path, figure, file)
                          for file in os.listdir(path + "/" + figure)
                          if file.endswith('.png')])
    return image_files
def img_loader(r, old):
    root_path = 'generator_figure/RaiymbekAgai'
    csvimg = []
    labels = []
    if r:
        triangle_load = loadImages(root_path, 'my_triangle2')
        square_load = loadImages(root_path, 'my_convex4_2')
        circle_load = loadImages(root_path, 'my_circle2')
        star_load = loadImages(root_path, 'my_star5_2')
        for image_file_name in triangle_load:
            label = 0
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in square_load:
            label = 1
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in circle_load:
            label = 2
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in star_load:
            label = 3
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        triangle_load = None
        square_load = None
        circle_load = None
        star_load = None
    if old:
        my_root_path = 'gradient_tabuu/100x100'
        my_triangle_load = loadImages(my_root_path, 'triangle')
        my_square_load = loadImages(my_root_path, 'square')
        my_circle_load = loadImages(my_root_path, 'circle')
        my_star_load = loadImages(my_root_path, 'star')


        for image_file_name in my_triangle_load:
            label = 0
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in my_square_load:
            label = 1
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in my_circle_load:
            label = 2
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        for image_file_name in my_star_load:
            label = 3
            img = cv2.imread(image_file_name, 0)
            csvimg.append(img)
            labels.append(label)
            pass
        my_triangle_load = None
        my_square_load = None
        my_circle_load = None
        my_star_load = None

    item_list = list(range(len(csvimg)))
    shuffle(item_list)
    shuffle(item_list)
    new_csvimg = []
    new_labels = []
    for item in item_list:
        new_csvimg.append(csvimg[item])
        new_labels.append(labels[item])

    return new_csvimg, new_labels
