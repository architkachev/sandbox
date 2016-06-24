import collections


def generate_horse_graph():
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

    graph = collections.defaultdict(list)
    for i in range(8):
        for j in range(8):
            graph[(i, j)].extend(get_acceptable_steps(i, j))

    return dict(graph)


def get_path(start_point, end_point, graph):
    pass

graph = generate_horse_graph()
sp = (0, 0)
ep = (7, 7)
print get_path(start_point=sp, end_point=ep, graph=graph)

