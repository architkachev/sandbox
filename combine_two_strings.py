from itertools import chain


def is_shuffle(str1, str2, str3):
    arr2 = [0] * 65536
    arr1 = [0] * 65536
    for i in str3:
        arr2[ord(i)] += 1
    for i in chain(str1, str2):
        arr1[ord(i)] += 1
    return arr1 == arr2


def is_shuffle2(str1, str2, str3):
    pass


a = "abdbvsdeexgbgdfsb"
b = "defdsfbvdfb esrg es serg serg serg es gesrgsrtgbdrt  ssetgesg"
c = "abdbvsdedefdsfbvdfb esrg es serg serg serg es gesrgsrtgbdrt  ssetgesgexgbgdfsb"

print is_shuffle(a, b, c)
