
import numpy as np


def compute_area(length, width):
    """Compute area of a square/rectangle"""
    return length*width


def main():

    length = 2.0
    width = 1.0

    area = compute_area(length, width)

    print("Area: ", area)

    return None


main()
