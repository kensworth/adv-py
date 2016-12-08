import sys
arr = [-1, 2, 4, 0]

def create_empty_tree(arr):
    if len(arr) != 0 and (len(arr) & (len(arr)- 1)) == 0:
        return [sys.maxint] * (2 * len(arr) - 1)
    else:
        return [sys.maxint] * (2 * next_power_of_two(len(arr)) - 1)

def next_power_of_two(num):
    power = 0
    while 2 ** power < num:
        power += 1
    return 2 ** power

def create_min_segment_tree(arr, segment_tree, low, high, pos):
    if low == high:
        segment_tree[pos] = arr[low]
        return
    mid = (low + high) // 2
    create_min_segment_tree(arr, segment_tree, low, mid, 2 * pos + 1)
    create_min_segment_tree(arr, segment_tree, mid + 1, high, 2 * pos + 2)
    segment_tree[pos] = min(segment_tree[2 * pos + 1], segment_tree[2 * pos + 2])

def range_min_query(segment_tree, q_low, q_high, low, high, pos):
    if q_low <= low and q_high >= high:
        # total overlap
        return segment_tree[pos]
    elif q_low > high or q_high < low:
        # no overlap
        return sys.maxint
    # partial overlap
    mid = (low + high) // 2
    min_left = range_min_query(segment_tree, q_low, q_high, low, mid, 2 * pos + 1)
    min_right = range_min_query(segment_tree, q_low, q_high, mid + 1, high, 2 * pos + 2)
    return min(min_left, min_right)

segment_tree = create_empty_tree(arr)
create_min_segment_tree(arr, segment_tree, 0, len(arr) - 1, 0)
minimum = range_min_query(segment_tree, 1, 3, 0, len(arr) - 1, 0)
print segment_tree
print minimum

