for i in range(10):
    print(i)
    for j in range(10):
        print(i, j)
        if i == j:
            break
    if i == 5:
        continue
    print(i)