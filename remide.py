

import bcrypt

listAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

listAll=[]

for cha1 in listAlpha:
    print("started " + cha1)
    for cha2 in listAlpha:
        for cha3 in listAlpha:
            for cha4 in listAlpha:
                for cha5 in listAlpha:
                    for cha6 in listAlpha:
                        s=cha1+cha2+cha3+cha4+cha5+cha6
                        print(s)
                        s = bcrypt.hashpw(str.encode(s), bcrypt.gensalt())
                        listAll.append(s)

    print("finish " + cha1)
for element in listAll:
    bcrypt.checkpw(str.encode("aaaaaa"), str.encode(element))