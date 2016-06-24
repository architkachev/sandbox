import collections
import string


def read_words(path):
    words = []
    with open(path) as file:
        for word in file:
            words.append(word.strip("\n"))
    return words


def get_all_words():
    return read_words("words/words.txt")


def get_10k_words():
    return read_words("words/words10k.txt")


def get_20k_words():
    return read_words("words/words20k.txt")


def construct_graph(list_words):
    """
    Precomputation for list words
    Example:
    >>> construct_graph(["cat", "bat", "at", "ad", "bet", "ed", "bed"])
    defaultdict(<type 'list'>, {'cat': ['at', 'bat']})
    """
    graph = collections.defaultdict(list)
    letters = string.lowercase
    for word in list_words:
        for i in range(len(word)):
            # remove 1 character
            removed = word[:i] + word[i + 1:]
            if removed in list_words:
                graph[word].append(removed)

            # change 1 character
            for char in letters:
                changed = word[:i] + char + word[i + 1:]
                if changed in list_words and changed != word:
                    graph[word].append(changed)

        # add 1 character
        for i in range(len(word) + 1):
            for char in letters:
                added = word[:i] + char + word[i:]
                if added in list_words:
                    graph[word].append(added)
        print "{0}\t: {1}".format(list_words.index(word), word)
    return graph
