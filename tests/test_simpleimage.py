#!/usr/bin/python3
# -*- coding: utf-8 -*-

import simpleimage as si


def test_constructor():
    image = si.SimpleImage((100, 100))
    assert(image != None)
