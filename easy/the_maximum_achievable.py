def the_maximum_achievable(num, t):
    x = 0
    while True:
        copy_x = x
        copy_num = num

        for i in range(0, t):
            copy_num += 1
            copy_x -= 1

        if copy_num == copy_x:
            return x

        x += 1


the_maximum_achievable(4, 1)
the_maximum_achievable(3, 2)
