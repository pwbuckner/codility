# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6

    binary = (bin(N)[2:])

    gap = 0

    count = 0

    print(binary)

    for x in binary:
        count = count + 1
        if int(x) == 1:
            if count > gap:
                gap = count-1
            count = 0

    print("x: ", x)
    print("count: ", count)
    print("gap: ", gap)
    pass


solution(74901729)