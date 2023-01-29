import sys


def main(algorithm, string_list):
    # convert every list item to int type
    unsorted_list = validate_list(string_list)

    if not unsorted_list:
        return
    elif algorithm == "insertion":
        insertion_sort(unsorted_list)
    else:
        print(f"can't sort using {algorithm}")


def validate_list(l):
    try:
        return [int(i) for i in l]
    except ValueError:
        print("list contains non-int element")
        return None

def insertion_sort(l):
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    print(l)


if __name__ == '__main__':
    if len(sys.argv) >   print(l2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")
