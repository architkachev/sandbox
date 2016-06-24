def check(expr):
    if len(expr) % 2 != 0:
        return False
    matcher = {("(", ")"), ("{", "}"), ("[", "]")}
    opened = set([x[0] for x in matcher])
    stack = []
    for char in expr:
        if char in opened:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (last, char) not in matcher:
                return False
    return len(stack) == 0

expr = "{()}"
expr2 = "([{{{}}}])"

print check(expr)
print check(expr2)
