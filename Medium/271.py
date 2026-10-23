def encode(strs):
    res = ""
    for i in strs:
        res += str(len(i)) + "#" + i
    return res

def decode(strs):
    res = []
    i = 0
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        length = int(strs[i:j])
        res.append(strs[j+1: j + 1 + length])
        i = j + 1 + length
    return res

strs = ["neet" , "code"]
print(encode(strs))
print(decode((encode(strs))))