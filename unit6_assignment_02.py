__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
4. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
5. Review the files lesson and write elegant code. Python api/features makes it possible to write concise and efficient code.
'''

import unit6utils

def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    f1=open(source,"rt")
    f2=open(destination,"wt")

    res=[]
    l=[]
    while True:
        line=f1.readline()
        #print(line)
        if not line:
            break
        l=line.lower().split()
        #print(l)
        if("#" in l or l==[]):
            continue
        else:
            res.extend(l)

    #print(res)
    res.sort(key=lambda i:i.lower())

    #print(res)

    #f2.write(" ".join(res))
    for i in res:
        f2.write(i+"\n")

def test_sort_words():
    source = unit6utils.get_input_file("unit6_testinput_02.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
    destination = unit6utils.get_temp_file("unit6_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    print(expected)
    print(result)
    assert expected == result
