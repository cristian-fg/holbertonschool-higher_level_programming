#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Function that find a peak"""
    if list_of_integers:
        ls = sorted(list_of_integers)
        return ls[-1]
