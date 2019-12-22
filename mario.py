from cs50 import get_int
# prompt user for correct imput
while True:
    x = get_int("Height: ")
    if x >= 1 and x <= 8:
        i = 1
        while i <= x:
            print(" " * (x-i) + "#"*i + "  " + "#"*i)
            i += 1
        break