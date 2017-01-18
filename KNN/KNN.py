from collections import Counter


def find_mode(aList):
    counter = Counter(aList)
    max_count = max(counter.values())
    final_arr = [k for k, v in counter.items() if v == max_count]
    print final_arr[0]

my_list = [1, 3, 4, 1, 4, 4]
find_mode(my_list)

