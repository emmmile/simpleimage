#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module implements a simple file name generator based on time and pid.
It is useful when generating multiple outputs in the same program, say:

image-20180810-141453-428772-10275.png
image-20180810-141458-348924-10275.png
...

I include it here because I use it for generative art, but it is of course
agnostic from the file format.
"""

import datetime
import os


class FileName():
    """This class does implements a simple file name generator."""
    def __init__(self,
                 name: str,
                 file_prefix: str = '',
                 file_format: str = '',
                 microseconds: bool = True) -> None:
        self.name = name
        self.file_prefix = file_prefix
        self.file_format = file_format
        self.microseconds = microseconds

    def __str__(self) -> str:
        now = datetime.datetime.now()
        time = now.strftime("%Y%m%d-%H%M%S")
        micros = now.strftime("-%f")
        pid = str(os.getpid())

        output = self.name + '-' + time
        if self.microseconds:
            output += micros
        output += '-' + pid
        if self.file_prefix:
            output = self.file_prefix + output
        if self.file_format:
            output = output + '.' + self.file_format
        return output

    def str(self):
        """Returns the next file name."""
        return FileName.__str__(self)
