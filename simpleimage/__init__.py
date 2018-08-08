import cv2
import logging
import datetime
import os


class FileName(object):
    def __init__(self, name, file_prefix='', file_format=''):
        self.name = name
        self.file_prefix = file_prefix
        self.file_format = file_format
        
    def __str__(self):
        now = str(datetime.datetime.now()).replace(':', '').replace('-', '').replace('.', '-').replace(' ', '-')
        pid = str(os.getpid())
        
        output = self.file_prefix + self.name + '-' + now + '-' + pid
        if self.file_format:
            output += '.' + self.file_format
        return output
    
    def str(self):
        return str(self)


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
