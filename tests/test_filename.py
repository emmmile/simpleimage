#!/usr/bin/python3
# -*- coding: utf-8 -*-

import simpleimage as si


def test_constructor():
    filename = si.FileName('')
    assert(filename != None)


def test_str():
    filename = si.FileName('')
    assert(str(filename) != None)
