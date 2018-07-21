__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
import string

def encrypt(text, key):
    if type(text).__name__!='str' or type(key).__name__!='str':
        raise TypeError("mismatch type")
    if key.isalpha()==False or key=="":
        raise ValueError

    d1=dict(zip(string.ascii_lowercase,range(26)))
    d2 = dict(zip(string.ascii_uppercase, range(26)))
    d1.update(d2)
    #d1 contains total dict

    res=""
    klen=len(key)
    x=0
    for i in text:
       if i.isalpha()==False:
           res=res+i
       else:
           temp=d1[key[x%klen]]+ord(i)
           if i.isupper()==True:
               if temp>90:
                   temp=64+(temp-90)%26
               res=res+chr(temp)
           else:
               if temp>122:
                   temp=96+(temp-122)%26
               res=res+chr(temp)
           x=x+1
    print(res)
    return res







def decrypt(text, key):
    if type(text).__name__ != 'str' or type(key).__name__ != 'str':
        raise TypeError("mismatch type")
    if key.isalpha() == False or key == "":
        raise ValueError

    d1 = dict(zip(string.ascii_lowercase, range(26)))
    d1.update(zip(string.ascii_uppercase, range(26)))

    res = ""
    klen = len(key)
    x = 0
    for i in text:
        if i.isalpha() == False:
            res = res + i
        else:
            temp =ord(i)-d1[key[x % klen]]
            if i.isupper() == True:
                if temp <65:
                    temp = -64+temp+90
                res = res + chr(temp)
            else:
                if temp <97:
                    temp = -96 + temp+122
                res = res + chr(temp)
            x = x + 1
    print(res)
    return res


def test_encrypt():
    assert "hj vkirf" == encrypt("hi there", "abcde")
    assert "hj *!Vkirf" == encrypt("hi *!There", "abcde")

    try:
        encrypt("hi there", {1:'a'})
        assert False, "Invalid type did not raise error"
    except TypeError as te:
        print(te)

    try:
        encrypt("hi there", "fwe1")
        assert False, "Invalid value did not raise error"
    except ValueError as te:
        print(te)
    #assert "hj vkfra" == encrypt("hi therz", " ")
    assert "ecuvgkwxovwlskg"==encrypt('mysecretmessage', 'secret')
    assert "ecuvgkwxovwlskg" == encrypt('mysecretmessage', 'SECret')
    assert "EcUvgkwxOvwlskg" == encrypt('MySecretMessage', 'secret')
    assert "Ec Uvgkwx 10:20 Ovwlskg" == encrypt('My Secret 10:20 Message', 'secret')





def test_decrypt():
    assert "hi therz" == decrypt("hj vkfra", "abcdb")
    assert "mysecretmessage" == decrypt('ecuvgkwxovwlskg', 'secret')
    assert "mysecretmessage" == decrypt('ecuvgkwxovwlskg', 'SECret')
    assert "MySecretMessage" == decrypt('EcUvgkwxOvwlskg', 'secret')
    assert "My Secret 10:20 Message" == decrypt('Ec Uvgkwx 10:20 Ovwlskg', 'secret')

