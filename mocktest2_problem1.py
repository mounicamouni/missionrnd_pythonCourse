max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''


def vowel_count_test(string):
    count = 0
    for z in string:
        if z in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
            count = count + 1
    return count


def transform(sentence):

    if not isinstance(sentence,str):
        raise TypeError
    l = sentence.split()
    for i in l:
        if i.isalpha() == False:
            raise ValueError

    '''l.sort()
    # vowel sort
    #print(l)
    l.sort(key=vowel_count_test, reverse=False)
    #print(l)
    l.sort(key=lambda s: len(s), reverse=True)
    '''
    l.sort(key=lambda x:x.lower())
    l.sort(key=vowel_count_test, reverse=False)
    l.sort(key=len,reverse=True)
    return " ".join(l)


def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway  ")
    assert "elephant waaaaing b A"==transform("waaaaing  elephant b A")
    assert "Elephants fast tour got Pat Run" == transform("Run tour Pat fast got Elephants")

    assert "" == transform("")
    try:
        transform({1:'v'})
        assert False, "Invalid type did not raise error"
    except TypeError as te:
        print(te)
    try:
        transform("cad 123")
        assert False, "Invalid type did not raise error"
    except ValueError as te:
        print(te)