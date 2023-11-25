from .labels import *


def display_data(data):
    print("Načtená data: ")
    for key in ORDER:
        if key in data:
            print(f"{key}: {data[key]}")
        else:
            print(f"{key}: Nenalezeno")