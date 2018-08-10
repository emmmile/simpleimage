#!/usr/bin/python3
# -*- coding: utf-8 -*-

from simpleimage import FileName


def test_constructor():
    filename = FileName('')
    assert(filename is not None)


def test_str_no_microseconds():
    filename = FileName('', microseconds=False)
    assert(str(filename) is not None)
    assert(filename.str() is not None)
    assert(str(filename) == filename.str())


def test_str():
    filename = FileName('')
    assert(len(str(filename)) == len(filename.str()))
    print(str(filename))
