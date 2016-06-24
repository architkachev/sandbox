import pickle


def get_graph():
    return pickle.load(open("words/graph.json", "rb"))