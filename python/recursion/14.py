count = 0
def greet():
    global count

    if count == 4:
        return
    count += 1
    print("head hello", count)

    greet()
    print("tail hello",count)
    count -= 1

greet()