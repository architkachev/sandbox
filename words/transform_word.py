import collections
import string
import pickle

from words.constants import read_words, get_10k_words, get_20k_words
from words.graph_provider import get_graph


def get_modifications(word, list_words):
    result = []
    letters = string.lowercase
    for i in range(len(word)):
        # remove 1 character
        removed = word[:i] + word[i + 1:]
        if removed in list_words and removed not in result:
            result.append(removed)

        # change 1 character
        for char in letters:
            changed = word[:i] + char + word[i + 1:]
            if changed in list_words and changed != word:
                result.append(changed)

    # add 1 character
    for i in range(len(word) + 1):
        for char in letters:
            added = word[:i] + char + word[i:]
            if added in list_words and added not in result:
                result.append(added)
    # print "{0}\t: {1}".format(list_words.index(word), word)
    return result

def get_list_mutations(word):
    result = []
    letters = string.lowercase
    for i in range(len(word)):
        # remove 1 character
        removed = word[:i] + word[i + 1:]
        if removed not in result:
            result.append(removed)

        # change 1 character
        for char in letters:
            changed = word[:i] + char + word[i + 1:]
            if changed != word and changed not in result:
                result.append(changed)

    # add 1 character
    for i in range(len(word) + 1):
        for char in letters:
            added = word[:i] + char + word[i:]
            if added not in result:
                result.append(added)
    return result


def transform(graph, start_vertex, end_vertex, path=[]):
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    if start_vertex not in graph:
        return None
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = transform(graph, vertex, end_vertex, path)
            if extended_path:
                return extended_path
    return None


def transformWord(graph, start, goal):
    paths = collections.deque([[start]])
    extended = set()
    while len(paths) != 0:
        currentPath = paths.popleft()
        currentWord = currentPath[-1]
        if currentWord == goal:
            return currentPath
        elif currentWord in extended:
            continue

        extended.add(currentWord)
        transforms = graph[currentWord]
        for word in transforms:
            if word not in currentPath:
                paths.append(currentPath[:] + [word])
    return []


# dictionary = ["cat", "bat", "at", "ad", "bet", "ed", "bed"]


# graph = dict(construct_graph(dictionary))
# print graph
# print transform(graph, "cat", "bed")

# pickle.dump(graph, open("words/graph.json", "wb"))
# graph = pickle.load(open("words/graph.json", "rb"))
# print graph2
# print get_modifications("apend", dictionary)

# print transformWord(get_graph(), "cat", "bed")


def get_hint(word):
    dictionary = get_20k_words()
    hints = get_modifications(word, dictionary)
    if not hints:
        mutations = get_list_mutations(word)
        print mutations
        for mutation in mutations:
            hint = get_modifications(mutation, dictionary)
            if hint is not None and hint not in hints:
                hints.append(hint)
    return hints

print get_hint("appritiate")