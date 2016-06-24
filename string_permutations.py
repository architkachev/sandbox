def permutations(string):
    if len(string) == 1:
        return [string]

    perms = permutations(string[1:])
    char = string[0]
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result

print permutations("ABC")