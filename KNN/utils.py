from collections import Counter


def find_mode(a_list):
    counter = Counter(a_list)
    max_count = max(counter.values())
    final_arr = [k for k, v in counter.items() if v == max_count]
    return final_arr[0]

