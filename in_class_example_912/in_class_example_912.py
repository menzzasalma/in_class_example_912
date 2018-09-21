# -*- coding: utf-8 -*-

"""Main module."""

def LargeIfFactual(s):
    ```returns the word big if the input says the word true

    ```
    if "true" in s:
        return "big"
    else:
        return "small"

a="true"
b="false"
c="anything else"

x=LargeIfFactual(a)
y=LargeIfFactual(b)
z=LargeIfFactual(c)
