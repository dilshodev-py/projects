def restoreString(s: str, indices) -> str:
    result = [0]*len(indices)
    for i in range(len(indices)):
        result[indices[i]] = s[i]
    return "".join(result)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

