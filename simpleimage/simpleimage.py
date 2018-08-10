#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import numpy as np


# One channel accumulation plot.
class SimpleImage(object):
    def __init__(self, size):
        # https://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
        self.image = np.zeros(size, np.uint32)
    
    def draw_point(self, point):
        pass
    
    def draw_points(self, points):
        pass
    
    def draw_line(self, start, end):
        pass
    
    def save(self, name, invert=False, gamma=None):
        logging.debug('Saving {}'.format(name))
        pass
