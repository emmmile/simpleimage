#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import logging


# 1 channel accumulation plot
class SimpleImage(object):
    def __init__(self, size):
        pass
    
    def draw_point(self, point):
        pass
    
    def draw_points(self, points):
        pass
    
    def draw_line(self, start, end):
        pass
    
    def save(self, name, invert=False, gamma=None):
        logging.debug('Saving {}'.format(name))
        pass
