__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''

import itertools
def unjumble(jumbled_text, n):
    if not isinstance(jumbled_text, str):
        raise TypeError
    if n <= 0:
        raise ValueError
    text = jumbled_text
    f = list(range(n, 0, -1))
    f.extend(list(range(1, n + 1)))
    temp = itertools.cycle(f)
    temp1=itertools.cycle(f)

    d = {}
    d1={}
    for i in range(1, n + 1):
        d[i] = 0
        d1[i]=[]
    pivot = 0
    while (len(text) != 0):
        z = temp.__next__()
        d[z]+=1
        text = text[pivot + z:]
    res = ""
    #print(d)
    text=jumbled_text
    pivot=0
    for i, j in d.items():
        for x in range(j):
            d1[i].append(text[pivot:pivot+i])
            text=text[pivot+i:]
    #print(d1)

    while True:
        try:
            z=temp1.__next__()
            #print(z)
            res=res+d1[z].pop(0)
        except:
            #print(res)
            return res




def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)
    assert "Ashokan" == unjumble("anokAsh", 3)
    assert "Ashokan" == unjumble("Ashokan", 1)
    assert "Mounica" == unjumble("caniMou", 3)
    assert "Mounica" == unjumble("unMoica", 2)
    assert "Programming" == unjumble("ngmiramProg", 4)
    try:
        unjumble({}, 2)
    except TypeError as te:
        print(te)

    try:
        unjumble("fsd", 0)
    except ValueError as te:
        print(te)