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


def load_img(r, old):
    length_figure = [0, 0, 0, 0]
    test_images = []
    test_labels = []
    if r:
        root_path = 'generator_figure/RaiymbekAgai'
        test_triangle_load = loadImages(root_path, 'my_triangle_test')
        test_square_load = loadImages(root_path, 'my_convex4_test')
        test_circle_load = loadImages(root_path, 'my_circle_test')
        test_star_load = loadImages(root_path, 'my_star5_test')
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
    if old:
        root_path = 'gradient_tabuu/100x100'
        test_triangle_load = loadImages(root_path, 'triangle_test')
        test_square_load = loadImages(root_path, 'square_test')
        test_circle_load = loadImages(root_path, 'circle_test')
        test_star_load = loadImages(root_path, 'star_test')
        i = 0
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
    # new_test_images = np.array(test_images) / 255

    return test_images, test_labels, length_figure
