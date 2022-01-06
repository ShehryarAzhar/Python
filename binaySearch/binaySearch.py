import random
import time

# ***** NAIVE_SEARCH *****
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i # returns the index of the target
    return -1 # if target isn't in the list returns -1


# ***** BINARY_SEARCH *****
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1

    midpoint = (low + high)  // 2 # (3/2 = 1.5) and (3//2 = 1)


    # we'll if target == l[midpoint] if it is, it returns the midpoint if not
    # we will check if target is greater than or less than midpoint
    # we know the list is sorted so,
    # if the target is less than l[midpoint] we know it's on the left side of midpoint
    # or if the target is greater than l[midpoint] we know it's on the right side of midpoint
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    


if __name__ == "__main__":
    length = 10000
    target_list = [random.randint(-3*length, 3*length) for _ in range(length)]
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(end-start)
    
    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(end-start)