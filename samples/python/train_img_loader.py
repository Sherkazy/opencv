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


def img_loader(r):
    root_path = 'dataset'
    csvimg = []
    labels = []
    type_figure = ''
    if r == 1:
        type_figure = '1px'
    elif r == 2:
        type_figure = '3px'
    else:
        type_figure = 'all'
    triangle_load = loadImages(root_path, 'triangle' + type_figure)
    square_load = loadImages(root_path, 'convex4_' + type_figure)
    circle_load = loadImages(root_path, 'circle' + type_figure)
    star_load = loadImages(root_path, 'star5_' + type_figure)
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

    item_list = list(range(len(csvimg)))
    shuffle(item_list)
    shuffle(item_list)
    new_csvimg = []
    new_labels = []
    for item in item_list:
        new_csvimg.append(csvimg[item])
        new_labels.append(labels[item])

    return new_csvimg, new_labels
