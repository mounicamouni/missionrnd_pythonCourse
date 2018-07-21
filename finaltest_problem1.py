__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''

import itertools
def repeats(digits):
    if not isinstance(digits,str):
        raise TypeError

    length = len(digits)
    x= [digits[i:j + 1] for i in range(length) for j in range(i, length)]

    res=[]
    #print(x)
    for i in x:
        if len(i)==1:
            continue
        count=digits.count(i)
        if(count>1):
            if (i,count) not in res:
                res.append((i,count))
    #print(res)
    #res=list(set(res))
    res.sort(key=lambda x:int(x[0]),reverse=True)
    res.sort(key=lambda x:x[1],reverse=True)

    print(res)
    return res

def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    assert [] == repeats("")
    assert [("11", 2)] == repeats("11111")
    assert [("11", 3),("111",2)] == repeats("111111")
    assert [("22", 2),("11",2)] == repeats("11112222")
    assert [('110', 2), ('022', 2), ('22', 2), ('011', 2), ('11', 2), ('10', 2), ('02', 2), ('01', 2)] == repeats("011011022022")
    try:
         repeats({1.2:3})
    except TypeError as te:
        print(te)

    try:
         repeats(None)
    except TypeError as te:
        print(te)