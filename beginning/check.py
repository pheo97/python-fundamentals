height = 5
for i in range(height):
    for j in range(i, height):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    print()
