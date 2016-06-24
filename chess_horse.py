import collections


def filter_steps():
    pass


def get_acceptable_steps(i, j):
    template = {(i + 1, j - 2), (i + 1, j + 2), (i - 1, j - 2),
                (i - 1, j + 2),
                (i + 2, j - 1), (i + 2, j + 1), (i - 2, j + 1),
                (i - 2, j - 1)}
    result = []
    for step in template:
        if step[0] < 0 or step[0] > 7 or step[1] < 0 or step[1] > 7:
            pass
        else:
            result.append(step)
    return result


def generate_horse_graph():
    graph = collections.defaultdict(list)
    for i in range(8):
        for j in range(8):
            graph[(i, j)].extend(get_acceptable_steps(i, j))

    return dict(graph)


def path(graph, start, goal):
    paths = collections.deque([[start]])
    extended = set()
    while len(paths) != 0:
        current_path = paths.popleft()
        current_point = current_path[-1]
        if current_point == goal:
            return current_path
        elif current_point in extended:
            continue
        extended.add(current_point)
        transforms = graph[current_point]
        for word in transforms:
            if word not in current_path:
                paths.append(current_path[:] + [word])
    return []


graph = generate_horse_graph()
# print graph
sp = (0, 0)
ep = (7, 7)

print path(graph, sp, ep)
