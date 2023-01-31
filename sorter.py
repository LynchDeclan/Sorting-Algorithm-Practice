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
        print(unsorted_list)
    elif algorithm == "insertion":
        insertion_sort(unsorted_list)
        print(unsorted_list)
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
    for first_elm in range(0, len(l)):
        min_val = first_elm
        for new_elm in range(min_val + 1, len(l)):
            if l[min_val] > l[new_elm]:
                min_val = new_elm
            l[first_elm], l[min_val] = l[min_val], l[first_elm] 
  

def insertion_sort(l):
    # Iterates through the list
    for i in range(1, len(l)):
        k = i
        # If the index value that is being checked is less than its neighbour to the left, 
        # and the index value is greater than the 0th, then swap them
        while l[k] < l[k-1] and k > 0:
            l[k], l[k-1] = l[k-1], l[k]
            k -= 1


    



if __name__ == '__main__':
    if len(sys.argv) > 2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")
