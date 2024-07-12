def imagelenght(string):
    res=0
    for letter in string:
        match letter:
            case " ":
                res+=1
            case "I":
                res+=3
            case "i":
                res+=3
            case "M":
                res+=5
            case "m":
                res+=5
            case "T":
                res+=5
            case "v":
                res+=5
            case "V":
                res+=5
            case _:
                res+=4
    return res

n=imagelenght("v ")
print(n)