def max_intersections_interval(list_intervals):
    def count_intersections(list_intervals, interval):
        count = 0
        for i in list_intervals:
            if i[1] > interval[0] and i[0] < interval[1]:
                count += 1
        return count

    result = list_intervals[0]
    max_count = 0
    for interval in list_intervals:
        count = count_intersections(list_intervals, interval)
        if count > max_count:
            max_count = count
            result = interval

    return result



l = [[0,6], [1, 8], [1, 6], [7, 10]]

print max_intersections_interval(l)
