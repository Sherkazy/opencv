from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras


def loadImages(path, figure):
    '''Put files into lists and return them as one list with all images
     in the folder'''
    image_files = sorted([os.path.join(path, figure, file)
                          for file in os.listdir(path + "/" + figure)
                          if file.endswith('.png')])
    return image_files


def load_img(r):
    length_figure = [0, 0, 0, 0]
    test_images = []
    test_labels = []
    root_path = 'dataset'
    type_figure = ''
    if r == 1:
        type_figure = '1px'
    elif r == 2:
        type_figure = '3px'
    else:
        type_figure = 'all'
    test_triangle_load = loadImages(root_path, 'triangle'+type_figure+'_test')
    test_square_load = loadImages(root_path, 'convex4_'+type_figure+'_test')
    test_circle_load = loadImages(root_path, 'circle'+type_figure+'_test')
    test_star_load = loadImages(root_path, 'star5_'+type_figure+'_test')
    for image_file_name in test_triangle_load:
        label = 0
        img = cv2.imread(image_file_name, 0)
        test_images.append(img)
        test_labels.append(label)
        pass
    for image_file_name in test_square_load:
        label = 1
        img = cv2.imread(image_file_name, 0)
        test_images.append(img)
        test_labels.append(label)
        pass
    for image_file_name in test_circle_load:
        label = 2
        img = cv2.imread(image_file_name, 0)
        test_images.append(img)
        test_labels.append(label)
        pass
    for image_file_name in test_star_load:
        label = 3
        img = cv2.imread(image_file_name, 0)
        test_images.append(img)
        test_labels.append(label)
        pass
    length_figure = [length_figure[0] + len(test_triangle_load), length_figure[1] + len(test_square_load),
                     length_figure[2] + len(test_circle_load), length_figure[3] + len(test_star_load)]
    test_triangle_load = None
    test_square_load = None
    test_circle_load = None
    test_star_load = None

    return test_images, test_labels, length_figure
