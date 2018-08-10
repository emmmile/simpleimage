#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module implements a simple file name generator based on time and pid."""

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
        time = now.strftime("%y%m%d-%H%M%S")
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
