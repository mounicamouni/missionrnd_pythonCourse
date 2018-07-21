__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
def to_custom_base5(number):
    if (isinstance(number, int) is False):
        raise TypeError
    res={0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u'}
    f = 0
    s=""
    if number < 0:
        f = 1
        number = abs(number)
    while (number != 0):
        rem = number % 5
        number = number // 5
        s = s + res[rem]
    if f == 1:
        s = s + '-'
    return s[::-1]

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):

    if (isinstance(s, str) is False):
        raise TypeError
    s=s.strip()
    set1=set(s)

    if (set(s)-set("+-aeiouAEIOU")!=set())or s=="":
        raise ValueError

    res={'a':0,'e':1,'i':2,'o':3,'u':4}

    f=0
    if(s[0]=='-'):
        f=-1
        s=s[1:]
    elif s[0]=='+':
        f=1
        s=s[1:]

    str1=""
    for i in s:
        i=i.lower()
        str1=str1+str(res[i])

    y=int(str1,5)

    if(f==-1):
        y=y*-1
    return y


# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)
    assert "ea" == to_custom_base5(5)
    assert "-ia" == to_custom_base5(-10)
    assert "-ea" == to_custom_base5(-5)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")
    assert -10 == from_custom_base5("-ia")
    assert 5 == from_custom_base5("ea")
    assert -5 == from_custom_base5("-ea")
    assert 5 == from_custom_base5(" +EA ")

    try:
        from_custom_base5(" -E A x")
        assert False, "Invalid string did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        from_custom_base5(123)
        assert False, "Invalid type did not raise error"
    except TypeError as te:
        print(te)
