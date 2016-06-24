def reverse1(string):
    return " ".join(reversed(string.split(" ")))


def reverse2(string):
    return " ".join(string.split(" ")[::-1])


def reverse3(string):
    words = []
    whitespaces = set(string.whitespace)

    index = 0
    for i in range(len(str)):
        if i not in whitespaces:
            index = i
        else:
            pass




string = "Interviews are awesome!"

print reverse2(string)