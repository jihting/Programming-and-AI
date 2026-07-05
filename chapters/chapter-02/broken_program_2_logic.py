# Week 2 Lab 3: deliberately broken logic program.
# This file runs, but some decisions are wrong.

score = int(input("Enter a score: "))

if score > 70:
    print("Strong pass")
elif score > 40:
    print("Pass")
else:
    print("Fail")

# Boundary cases to check:
# 70 should probably count as a strong pass in this exercise.
# 40 should probably count as a pass.
