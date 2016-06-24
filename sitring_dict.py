def split_sentence(inpt, ls):
    result = []
    s = 0
    for i in range(len(inpt)):
        try:
            ind = ls.index(inpt[s:i])
            result.append(ls[ind])
            s = i
        except ValueError:
            pass
    return result

s = "iamastudentfromwaterloo"
a = ["i", "am", "a", "student", "from", "waterloo"]

# print s[0:23]
# print a.index(a[0:1])

print split_sentence(s, a)
