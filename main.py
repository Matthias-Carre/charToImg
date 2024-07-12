from PIL import Image, ImageDraw, ImageFilter

pos=1

def imagelenght(string):
    res=0
    for letter in string:
        match letter:
            case " ":
                res+=2
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
        res+=1
    return res

def letterPosition(letter): #return (pos,lenght,isMaj)
    Lmin=[1,6,11,16,21,26,31,36,41,43,47,52,55,61,66,71,76,81,86,91,96,101,107,113,118,123,128]
    Lmax=[1,6,11,16,21,26,31,36,41,45,50,55,60,66,71,76,81,86,91,96,102,107,113,119,124,129,135]

    if(letter == " "):
        return (135,1,True)
    val=ord(letter)-64

    if(val<=26):
        return(Lmax[val-1],Lmax[val]-Lmax[val-1]-1,True)
    else:
        val=ord(letter)-96
        return (Lmin[val-1],Lmin[val]-Lmin[val-1]-1,False)
    

def addLetter(letter,image):
    global pos
    
    letterPos,letterLenght,isMaj = letterPosition(letter)
    if(isMaj):
        alphabet = Image.open("alphabetMaj.png")
    else:
        alphabet = Image.open("alphabetMin.png")
    mask_letter = Image.new("L",alphabet.size,0)
    draw = ImageDraw.Draw(mask_letter)
    draw.rectangle((letterPos,1,letterPos+letterLenght,9),fill=255)
    image.paste(alphabet,(pos-letterPos,0),mask_letter)
    pos+=letterLenght+1
    #print(f"valeur de pos et taille:{letterPos}, {letterLenght}")
    
    

def writemsg(msg):
    test=Image.new("RGBA",(imagelenght(msg),10),color=255)
    for e in msg:
        addLetter(e,test)
    test.save("res.png")


try :
    #writemsg("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    writemsg("voila")
except IndexError:
    print("indexerror")


