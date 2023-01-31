import sys

def main(algorithm, string_list):
    # convert every list item to int type
    unsorted_list = validate_list(string_list)
    
    if not unsorted_list:
        return
    if algorithm == "bubble":
        bubble_sort(unsorted_list)
        print(unsorted_list)
    else:
        print(f"can't sort using {algorithm}")

def validate_list(l):
    try:
        return [int(i) for i in l]
    except ValueError:
        print("list contains non-int element")
        return None


def bubble_sort(unsorted_list):
    list_sorted = False

    while list_sorted == False:
        list_sorted = True
        for i in range(0, len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                list_sorted = False
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp 
    
    return unsorted_list
                

if __name__ == '__main__':
    if len(sys.argv) > 2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")