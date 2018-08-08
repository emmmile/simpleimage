#!/usr/bin/python3
# -*- coding: utf-8 -*-

from simpleimage import FileName

def test_constructor():
    filename = FileName('')
    assert(filename != None)


def test_str():
    filename = FileName('')
    assert(str(filename) != None)
