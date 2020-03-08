
import numpy as np


def print_info():
    """Print info to user"""
    print("""Hello, this script helps you compute the area,volume 
             and perimeter of a rectangle""")
    return None

def compute_perimeter(length, width):
    """Compute perimeter of rectangle"""
    return 2*length+2*width


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

    perimeter = compute_perimeter(length, width)
    print("Perimeter:", perimeter)

    return None


main()
