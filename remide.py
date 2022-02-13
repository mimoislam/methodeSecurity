


import bcrypt
import json
import os.path
s = os.path.isfile('data.json')
listAll = []
if  s:
    print("Read file which has rainbow table")

    f = open('data.json')

    listAll = json.load(f)


else:
    print("creating file with rainbow table")
    listAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for cha1 in listAlpha:
        print("started " + cha1)
        for cha2 in listAlpha:
            for cha3 in listAlpha:
                for cha4 in listAlpha:

                    s = bcrypt.hashpw((cha1+cha2+cha3+cha4).encode('utf8'), bcrypt.gensalt())
                    listAll.append({"Hash":(s).decode('utf8'),"Password":str(cha1+cha2+cha3+cha4)})
                    print(len(listAll))

        print("finish " + cha1)

    json_string = json.dumps(listAll)
    with open('data.json', 'w') as outfile:
        outfile.write(json_string)
valid=False
for element in listAll:
    valid=bcrypt.checkpw(str.encode("aaab"), str.encode(element["Hash"]))
    if valid:
        print("we found the password . it is "+element["Password"])
        break

if not valid:
    print("We didn't find the password With Hash please change the crypto Algorithm ")