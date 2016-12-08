arr = [1, 2 , 3, 4, 5]
def power_set(arr):
    results = [[]]
    for num in arr:
        new_sets = [result + [num] for result in results]
        results.extend(new_sets)
    return results

def power_set_yield(arr):
    if arr == []:
        yield []
    else:
        for num in power_set_yield(arr[1:]):
            yield num + [arr[0]]
            yield num
