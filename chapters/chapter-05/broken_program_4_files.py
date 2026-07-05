# Week 2 Lab 3: deliberately broken file program.
# This program should read a file and print its contents.
# It needs a clear FileNotFoundError message.

filename = "missing_notes.txt"

with open(filename, "r") as file:
    contents = file.read()

print(contents)
