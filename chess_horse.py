import collections


def get_acceptable_steps(i, j):
    template = {(i + 1, j - 2), (i + 1, j + 2), (i - 1, j - 2),
                (i - 1, j + 2),
                (i + 2, j - 1), (i + 2, j + 1), (i - 2, j + 1),
                (i - 2, j - 1)}
    result = set()
    for step in template:
        if step[0] < 0 or step[0] > 7 or step[1] < 0 or step[1] > 7:
            pass
        else:
            result.add(step)
    return result


def generate_horse_graph():
    graph = collections.defaultdict(set)
    for i in range(8):
        for j in range(8):
            graph[(i, j)] = graph[(i, j)] | get_acceptable_steps(i, j)

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


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


graph = generate_horse_graph()
# print graph
sp = (0, 0)
ep = (7, 7)

# print path(graph, sp, ep)
gen = bfs_paths(graph, sp, ep)
print gen.next()
print gen.next()
print gen.next()