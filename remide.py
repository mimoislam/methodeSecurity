


import bcrypt

listAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v','w', 'x', 'y', 'z',"1","2", "3", "4", "5", "6", "7", "8", "9"]

listAll=[]

for cha1 in listAlpha:
    print("started " + cha1)
    for cha2 in listAlpha:
        for cha3 in listAlpha:
            for cha4 in listAlpha:
                s=cha1+cha2+cha3+cha4
                print(s)
                s = bcrypt.hashpw(str.encode(s), bcrypt.gensalt())
                listAll.append(s)

    print("finish " + cha1)
for element in listAll:
    bcrypt.checkpw(str.encode("aaaaaa"), str.encode(element))