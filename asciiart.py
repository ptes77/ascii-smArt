# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:34:22 2019

@author: eshao
"""

import numpy as np
import matplotlib.image as image

'''
# [DONE: 12:00PM] TODO: Correctly convert each pixel to grayscale
# [DONE: 1:00PM]  TODO: Convolution? Size of pixels must be determined
# [DONE: 1:18PM]  TODO: Import grayscale-to-ascii conversion
# [DONE: 1:34PM]  TODO: Return converted image
# TODO: Bounding edge on face (identify face)
# TODO: Set background to white/lowest value
# TODO: Convert to png/jpeg option
'''
    
def rgb_to_gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def compact(gray, pixel_size):
    if pixel_size <= 0:
        raise ValueError('Pixel size must be greater than 0!')
    height = len(gray)
    width = len(gray[0])
    pixel_size = min(pixel_size, height, width)
    compact = np.empty((height // (2 * pixel_size), width // pixel_size))
    for row in range(len(compact)):
        for col in range(len(compact[0])):
            img_slice = gray[2 * pixel_size * row:2 * pixel_size * (row + 1),
                             pixel_size * col:pixel_size * (col + 1)]
            avg_gray = np.sum(img_slice) / (pixel_size ** 2)
            compact[row][col] = avg_gray
    return compact

def convert(compact, conversion):
    res = ''
    for row in compact:
        for val in row:
            if val >= 1:
                res += conversion[len(conversion) - 1]
            else:
                val = int(val * len(conversion))
                res += conversion[val]
        res += '\n'
    return res[:-1]


if __name__ == '__main__':
    img = image.imread('D:\\Pictures\\Steve\\steve.png')
    gray = rgb_to_gray(img)
    try:
        pixel_size = int(input("Enter pixel size"))
    except:
        pixel_size = 2
    rmp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.'"
    ramp = dict()
    for i, char in enumerate(rmp):
        ramp[i] = char
    
    compact_values = compact(gray, pixel_size)
    art = convert(compact_values, ramp)
    with open('D:\\Pictures\\test_steve.txt', 'w') as f:
        f.write(art)
