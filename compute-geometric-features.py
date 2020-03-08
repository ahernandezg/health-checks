
import numpy as np

def print_info():
    """Print info to user"""
    print("""Hello, this script helps you compute the area,volume 
             and perimeter of a rectangle""")
    return None


def compute_volume(area, height):
    """"Compute volume of rectangle"""
    return area*height


def compute_area(length, width):
    """Compute area of a square/rectangle"""
    return length*width


def main():

    length = 2.0
    width = 1.0

    area = compute_area(length, width)
    print("Area: ", area)

    height = 2.0
    volume = compute_volume(area, height)
    print("Volume:", volume)

    return None


main()
