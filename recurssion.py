count = 0


def head_recurssion():
    global count
    if count == 4:
        return
    count += 1
    head_recurssion()
    print("Harsh")


head_recurssion()


def tail_recurssion():
    global count
    if count == 4:
        return
    count += 1
    print("Harsh")
    tail_recurssion()


tail_recurssion()
