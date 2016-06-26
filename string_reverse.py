s = "ABCDEF"

print(s[::-1])

def reverse(s):
    result = []
    for i in s:
        result.insert(0, i)
    return result

print(reverse(s))