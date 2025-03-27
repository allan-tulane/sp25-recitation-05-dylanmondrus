import random, time
import tabulate


def ssort(L):
    ### selection sort
    if len(L) <= 1:
        return (L)
    else:
        m = L.index(min(L))
        # print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        # print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])


def qsort(a, pivot_fn):
    ## TO DO
    if len(a) <= 1:
        return a

    pivot = pivot_fn(a)
    a = a[:]  # make a copy to avoid modifying original
    a.remove(pivot)
    less = [x for x in a if x <= pivot]
    greater = [x for x in a if x > pivot]
    return qsort(less, pivot_fn) + [pivot] + qsort(greater, pivot_fn)

    pass


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist.copy())  # copy to avoid in-place sorting effects
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000], input_type="random"):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    ### TODO - sorting algorithms for comparison
    def pivot_first(lst):
        return lst[0]

    def pivot_random(lst):
        return random.choice(lst)

    qsort_fixed_pivot = lambda lst: qsort(lst, pivot_first)
    qsort_random_pivot = lambda lst: qsort(lst, pivot_random)
    tim_sort = lambda L: sorted(L)
    selection_sort = lambda L: ssort(L)  # wrapper for consistency

    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        if input_type == "random":
            random.shuffle(mylist)

        # Skip selection sort on large inputs to avoid recursion depth errors
        if size <= 5000:
            ssort_time = time_search(selection_sort, mylist)
        else:
            ssort_time = None  # or "N/A" if preferred

        result.append([
            size,
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),
            ssort_time
        ])
        return result
    ###


def print_results(results, label=""):
    """ change as needed for comparisons """
    print(f"\n### Results: {label} ###")
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim-sort', 'ssort'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_print():
    random_results = compare_sort(input_type="random")
    print_results(random_results, "Random Inputs")

    sorted_results = compare_sort(input_type="sorted")
    print_results(sorted_results, "Sorted Inputs")


random.seed()
test_print()
