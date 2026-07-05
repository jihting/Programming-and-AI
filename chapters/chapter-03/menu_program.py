"""Week 2 Lab 1 starter: monolithic menu program for refactoring.

This program works, but it is intentionally written as one long script.
Your task is to refactor it into small functions.
"""

import math

running = True

while running:
    print("Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        radius_text = input("Radius: ")
        radius = float(radius_text)
        area = math.pi * radius * radius
        print("Circle area:", round(area, 2))
    elif choice == "2":
        width_text = input("Width: ")
        height_text = input("Height: ")
        width = float(width_text)
        height = float(height_text)
        area = width * height
        print("Rectangle area:", round(area, 2))
    elif choice == "3":
        print("Goodbye")
        running = False
    else:
        print("Invalid choice")
