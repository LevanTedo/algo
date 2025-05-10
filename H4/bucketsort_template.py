import random

def qsort_h(l, start, end):
    '''
    helper function to sort list l from index start to end (not included)
    '''
    if end - start > 1:
        pivot = l[start]
        m = start
        for i in range(start + 1, end):
            if l[i] < pivot:
                m = m + 1
                l[m], l[i] = l[i], l[m]  # swap l[i] and l[m]
        l[start], l[m] = l[m], l[start]
        qsort_h(l, start, m)
        qsort_h(l, m + 1, end)

def quicksort(l):
    '''
    sorts the given list l with the quicksort algorithm
    this function mutates the given list
    '''
    qsort_h(l, 0, len(l))


'''
Helper function for Bucketsort: Distribute values from list l
evenly to k buckets. The i-th bucket should contain values x
with x_min + i*dx <= x < x_min + (i+1)*dx where x_min, x_max
are the minimal and maximal value from l respectively and
dx = (x_max - x_min) / k is the width of each bucket.
'''
def distribute_buckets(l, k):
    min = 0
    max = 0
    for x in l:
        if x > max:
            max = x
        elif x < min:
            min = x
    bucketsize = (max-min)/k
    bucketlists = []
    
    for i in range(k-1):
        b_i = []
        lower_bound = min + i*bucketsize
        upper_bound = min + (i+1)*bucketsize
        for j in l:
            if lower_bound <= j and j < upper_bound:
                b_i.append(j)
        bucketlists.append(b_i)

    lastbucket = []
    for y in l:
        if y >= min + (k-1)*bucketsize:
            lastbucket.append(y) 
    bucketlists.append(lastbucket)

    return bucketlists

'''
Helper function for Bucketsort: Sort and concatenate buckets.
'''
def merge_buckets(buckets):
    result = []
    for x in buckets:
        quicksort(x)
        for i in x:
            result.append(i)
    return result

'''
Sort list l with Bucketsort algorithm using k buckets.
Creates a new list. We assume that l contains only numbers.
'''
def bucketsort(l, k):
    result = merge_buckets(distribute_buckets(l,k))
    return result


def randlist(n, a, b):
    '''
    generate a list of length n with random elements between a and b
    '''
    res = []
    for i in range(n):
        res.append(random.randint(a, b))
    return res


# Test program

l = [1, 2, 0, 2, 6, 4, 8, 7]
print(l)
l = bucketsort(l,4)
print(l)
