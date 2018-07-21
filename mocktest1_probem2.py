__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):

    if not isinstance(word,str):
        raise TypeError

    if word!="" and word.isalpha()==False:
        raise ValueError

    j=len(word)-1
    x=j #x gives the starting index of the palindrome
    flag=0
    for i in range(j):
        c=word[i].lower()
        d=word[j].lower()
        if c==d:
            flag=1
            j=j-1
            if x>i:
                x=i
        else:
            if flag==1:
                flag=0
                i=i-1
            j = len(word) - 1
            x = j

    for i in range(x-1,-1,-1):
        word=word+word[i].lower()

    return word

# write your own tests
def test_smallest_palindrome():
    assert 'mAlayalam'==smallest_palindrome("mAlaya")
    assert 'MAlayalam' == smallest_palindrome("MAlaya")
    assert 'MAlayalam' == smallest_palindrome("MAlaya")
    assert 'MAlayalamalayalam' == smallest_palindrome("MAlayalama")
    assert '' == smallest_palindrome("")
    try:
        smallest_palindrome("dw324")
        assert False, "Invalid string did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        smallest_palindrome({1: 2})
        assert False, "Invalid type did not raise error"
    except TypeError as te:
        print(te)
    try:
        smallest_palindrome(None)
        assert False, "Invalid type did not raise error"
    except TypeError as te:
        print(te)