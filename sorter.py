import sys


def main(algorithm, string_list):
    # convert every list item to int type
    unsorted_list = validate_list(string_list)

    if not unsorted_list:
        return
    if algorithm == "bubble":
        bubble_sort(unsorted_list)
    elif algorithm == "selection":
        selection_sort(unsorted_list)
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


def bubble_sort(l):
    # your code here
    print(l)


def selection_sort(l):
    # your code here
    print(l)


def insertion_sort(l):
    print(l)
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    else:
        pass
    print(l)
    if l[1] > l[2]:
        l.insert(1, l[2])
        del l[3]
    else:
        pass
    print(l)
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    else:
        pass
    print(l)
    if l[2] > l[3]:
        l.insert(2, l[3])
        del l[4]
    else:
        pass
    print(l)
    if l[1] > l[2]:
        l.insert(1, l[2])
        del l[3]
    else:
        pass
    print(l)
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    else:
        pass
    print(l)
    if l[3] > l[4]:
        l.insert(3, l[4])
        del l[5]
    else:
        pass
    print(l)
    if l[2] > l[3]:
        l.insert(2, l[3])
        del l[4]
    else:
        pass
    print(l)
    if l[1] > l[2]:
        l.insert(1, l[2])
        del l[3]
    else:
        pass
    print(l)
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    else:
        pass
    print(l)
    if l[4] > l[5]:
        l.insert(4, l[5])
        del l[6]
    else:
        pass
    print(l)
    if l[3] > l[4]:
        l.insert(3, l[4])
        del l[5]
    else:
        pass
    print(l)
    if l[2] > l[3]:
        l.insert(2, l[3])
        del l[4]
    else:
        pass
    print(l)
    if l[1] > l[2]:
        l.insert(1, l[2])
        del l[3]
    else:
        pass
    print(l)
    if l[0] > l[1]:
        l.insert(0, l[1])
        del l[2]
    else:
        pass
    print(l)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")
