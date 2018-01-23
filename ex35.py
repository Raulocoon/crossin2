i = 0
while i < 5:
    i += 1

    for j in range(3):
        print("j ---->>>> %d" % j)
        if j == 2:
            break

    for k in range(3):
        if k == 2 :
            continue

        print("k ====>>>> %d" %k)

    if i > 3:
        break

    print("i ****>>>> %d" %i)