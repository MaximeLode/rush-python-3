def alpha():
    original = "abcdefghijklmnopqrstuvwxyz" * 10
    n = 0
    while True:
        for j in range(n + 1):
            if n * (n + 1) // 2 + j >= len(original):
                exit()
            print(original[n * (n + 1) // 2 + j], end="")
        print()
        n += 1


alpha()