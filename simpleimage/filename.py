#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
