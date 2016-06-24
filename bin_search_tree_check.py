class Node(object):
    def __init__(self, val):
        self.left, self.right, self.val = None, None, val


MINUS_INF = float("-infinity")
PLUS_INF = float("infinity")


def check_tree(tree, min_val=MINUS_INF, max_val=PLUS_INF):
    if tree is None:
        return True

    if not min_val <= tree.val <= max_val:
        return False

    return check_tree(tree.left, min_val, tree.val) and \
           check_tree(tree.right, tree.val, max_val)


