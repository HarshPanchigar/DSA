def encode(strs):
    newStrs = ""
    for i in strs:
        newStrs += str(len(i)) + "#" + i
    return newStrs

def decode(s):
    res , i = [] , 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        lengh = 

strs = ["Hello","World"]
print(encode(strs))
print(decode(encode(strs)))