#!/usr/bin/python3
# -*- coding: utf-8 -*-

from simpleimage import SimpleImage


def test_constructor():
    image = SimpleImage((100, 100))
    assert(image != None)
