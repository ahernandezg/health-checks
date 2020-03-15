
import numpy as np
import matplotlib.pyplot as plt
import csv

def feature_d():
    
    return None


def compute_new_area():


def compute_new_feature():


    return None

def feature_b():
    
    return None

def menu():
    "Show a operations menu"
    print("1......compute area")
    print("2......compute volume")
    print("3......compute perimeter")
    choice = input("Choose an option:")
    return choice

def print_info():
    """Print info to user"""
    print("""Hello, this script helps you compute the area,volume
             and perimeter of a rectangle""")
    return None

def compute_perimeter(length, width):
    """Compute perimeter of rectangle"""
    return 2*length+2*width


def compute_volume(length, width, height):
    """"Compute volume of rectangle"""
    return length*width*height


def compute_area(length, width):
    """Compute area of a square/rectangle"""
    return length*width

def feature_a():

    return None




def main():

    length = 2.0
    width = 1.0

    choice = menu()
    if choice in '1':
        area = compute_area(length, width)
        print("Area: ", area)

    elif choice in '2':
        height = 2.0
        volume = compute_volume(length, width, height)
        print("Volume:", volume)

    elif choice in '3':
        perimeter = compute_perimeter(length, width)
        print("Perimeter:", perimeter)

    return None


main()
