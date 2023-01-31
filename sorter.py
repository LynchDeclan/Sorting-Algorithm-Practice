import sys


def main(algorithm, string_list):
    # convert every list item to int type
    unsorted_list = validate_list(string_list)

    if not unsorted_list:
        return
    if algorithm == "bubble":
        bubble_sort(unsorted_list)
        print("This is the sorted list:")
        print(unsorted_list)
    elif algorithm == "selection":
        selection_sort(unsorted_list)
        print("This is the sorted list:")
        print(unsorted_list)
    elif algorithm == "insertion":
        insertion_sort(unsorted_list)
        print("This is the sorted list:")
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
        print(unsorted_list)
        list_sorted = True
        for i in range(0, len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                list_sorted = False
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp 
    
    return unsorted_list


def selection_sort(l):
    for first_elm in range(0, len(l)):
        min_val = first_elm
        for new_elm in range(min_val + 1, len(l)):
            if l[min_val] > l[new_elm]:
                min_val = new_elm
        l[first_elm], l[min_val] = l[min_val], l[first_elm]
        print(l) 
  

def insertion_sort(l):
    # This is the part of the code that I (Declan) worked on
    for i in range(1, len(l)):
        k = i
        while l[k] < l[k-1] and k > 0:
            l[k], l[k-1] = l[k-1], l[k]
            print(l)
            k -= 1


    



if __name__ == '__main__':
    if len(sys.argv) > 2:
        # separate the algorithm name from the list elements
        main(sys.argv[1], sys.argv[2:])
    else:
        print("usage: sorter.py algorithm_name elem0 elem1 elem2...")
