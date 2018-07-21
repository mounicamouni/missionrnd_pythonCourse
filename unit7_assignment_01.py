__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""

import sys
import unit6utils

def anagram_sort(source,destination):
    f1 = open(source, "rt")
    f2 = open(destination, "wt")

    l = []
    res=[]
    l = f1.read().splitlines()
    # print(l)
    for i in l:
        if (i.split()[0] == "#"):
            l.remove(i)
    l = list(filter(None, l))
    #print(l)

    for i in l:
        temp=[]
        for j in l[l.index(i)+1:]:
            if(sorted(i.lower())==sorted(j.lower())):
                temp.append(j)
                l.remove(j)
        temp.append(i)
        temp.sort(key=lambda x:x.lower())
        res.append(temp)

    res.sort(key=lambda x:x[0].lower())
    res.sort(key=len,reverse=True)


    for i in res:
        for j in i:
            f2.write(j+'\n')
            print(j)




if __name__ == "__main__":
    x = input()
    z=x.split('.')
    z=z[0]+"-result.txt"

    destination = unit6utils.get_temp_file(z)
    anagram_sort(x,destination)

    #sys.exit(main())