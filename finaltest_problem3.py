__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
For this problem you have to implement a staircase jumble as described below. 

1. You have n stairs numbered 1 to n. You are given some text to jumble.
2. You repeatedly climb down and up the stairs and on each step k you add/append starting k chars from 
   the text you have (and remove them from the text). 
3. You repeat this process till you finish the whole text.
4. Finally you climb up from step 1 and collect all chars to get the jumbled text.

E.g.  if the text is "Ashokan" and n = 2.  You have the following text on the steps. First you drop 

 "As" on step 2, then "h" on step 1, then you get to the ground and you 
 climb back again droping "o" on step 1 and "ka" on step2 and finally "n" on step2 
 (since you have run out of chars and you dont have 2 chars).
  
 So sequence of steps is 2, 1 then 1, 2 then 2, 1 and so on...
 
(step2)As;ka;n
       ----
   (step 1)|h;o
           ----
Final jumbled text is hoAskan (all text on step1 followed by all text on step2, the ; is shown above only to visually 
distinguish the segments of text dropped on the stair at different times)

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Note that spaces, punctuation or any other chars are all treated like regular chars and 
   they will be jumbled in same way.
'''
import itertools
def jumble(text, n):

    if not isinstance(text,str):
        raise TypeError
    if n<=0:
        raise ValueError
    f=list(range(n,0,-1))
    f.extend(list(range(1,n+1)))
    temp=itertools.cycle(f)

    d={}
    for i in range(1,n+1):
       d[i]=[]
    pivot=0
    while(len(text)!=0):
        z=temp.__next__()
        d[z].append(text[pivot:pivot+z])
        text=text[pivot+z:]
    res=""
    for i in d.values():
        for j in i:
            res=res+j
    return res





def test_jumble():
    assert "hoAskan" == jumble("Ashokan", 2)
    assert "anokAsh" == jumble("Ashokan", 3)
    assert "Ashokan" == jumble("Ashokan", 1)
    assert "caniMou" == jumble("Mounica", 3)
    assert "unMoica" == jumble("Mounica", 2)
    assert "u Monica" == jumble("Mou nica", 2)
    assert "ngmiramProg"==jumble("Programming",4)
    assert "    " == jumble("    ", 4)
    try:
        jumble({}, 2)
    except TypeError as te:
        print(te)

    try:
        jumble("fsd", 0)
    except ValueError as te:
        print(te)