a = ["a1", "a2", "a3", "a4",     "b1", "b2", "b3", "b4",     "c1", "c2", "c3", "c4"]

target = ["a1", "b1", "c1",     "a2", "b2", "c2",     "a3", "b3", "c3",     "a4", "b4","c4"]

N = 4
l = len(a)  # 12


def get_index1(N, index):
    cur_section = index / N
    print "cur_sec {0}".format(cur_section)
    cur_position = index % N
    print "cur_pos {0}".format(cur_position)
    print "targ_sec {0}".format(cur_position)
    print "targ_pos {0}".format(cur_section)
    target_section = cur_position
    res = target_section * 3 + cur_section
    print "res_pos {0}".format(res)
    print ""
    return res


def get_index(groups, N, index):
    cur_section = index / groups
    print "cur_sec {0}".format(cur_section)
    cur_position = index % groups
    print "cur_pos {0}".format(cur_position)
    print "targ_sec {0}".format(cur_position)
    print "targ_pos {0}".format(cur_section)
    target_section = cur_position
    res = target_section * N + cur_section
    print "res_pos {0}".format(res)
    print ""
    # return res
    return index % groups * N + index / groups


def get_array(arr, groups):
    N = len(arr) / groups
    return [arr[get_index(groups, N, i)] for i in range(len(arr))]


print get_array(a, 3)
