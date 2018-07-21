__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''


def left_binary_search(input, value):
    if input==None or input==[] or value==None:
        return -1
    inp=list(input)
    l,r=0,len(input)-1
    res=-1
    while l<=r:
        mid=int((l+r)/2)
        if inp[mid]==value:
            r = mid - 1
            res=mid
        elif inp[mid]>value:
            r=mid-1
        else:
            l=mid+1
    return res
# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert -1 == left_binary_search(range(0, 10), -10)
    assert 0 == left_binary_search([1,1,1,1,1,1,1,1], 1)
    assert -1 == left_binary_search(None, 10)
    assert 2 == left_binary_search([1,2,3,3,4,4,5], 3)

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
