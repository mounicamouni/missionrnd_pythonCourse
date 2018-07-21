__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    if str1==None or str2==None:
        return None
    if len(str1)!=len(str2):
        return -1
    str2=str2*2
    x=str2.find(str1)
    return x


# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")
    assert 2 == get_right_rotations("mounica", "camouni")
    assert 4 == get_right_rotations("mounica", "nicamou")
    assert None==get_right_rotations(None, "camouni")
