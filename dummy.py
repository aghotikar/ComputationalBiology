def overlaps1(a, b):
    for i in range(1, min(len(a), len(b))):
        if a[-i:] == b[:i]:
            print(a + b[i:])


def overlaps2(a, b):
    overlaps1(a, b)
    overlaps1(b, a)


overlaps2('bbb', 'bbab')