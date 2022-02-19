


import bcrypt
import json
import os.path
from tkinter import *



Password =""

def Loading_List():
	listAll = []
	s = os.path.isfile('data.json')

	if  s:
		print("Read file which has rainbow table")

		f = open('data.json')

		return json.load(f)

	else:
        
		print("creating file with rainbow table")
		listAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
						 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

		for cha1 in listAlpha:
			print("started " + cha1)
			for cha2 in listAlpha:
				for cha3 in listAlpha:
					s = bcrypt.hashpw((cha1+cha2+cha3).encode('utf8'), bcrypt.gensalt())
					listAll.append({"Hash":(s).decode('utf8'),"Password":str(cha1+cha2+cha3)})
					print(len(listAll))
			print("finish " + cha1)

		json_string = json.dumps(listAll)

		with open('data.json', 'w') as outfile:
			outfile.write(json_string)
		return listAll


def Cracking (hash):
	listAll = []
	listAll = Loading_List()
	print(len(listAll))
	
	for element in listAll:
		print(element)
		print(str.encode(hash))
		valid = bcrypt.checkpw( str.encode(element["Password"]),str.encode(hash))
		if valid:
			print("Password Found ==> " + element["Password"])
			Password = (element["Password"])
			result.config(text = "Password Found:  "+element["Password"],fg='#fff',bg='#5BE62F')
			break
			
			

	if not valid:

		print("We didn't find the password With Hash please change the crypto Algorithm ")
		result.config(text = "Password Found not found")
		Password = ""
		result.config(text = "Sorry!! Password not found",fg='#fff',bg='Red')




def Matching (text):
	listAll = []
	listAll = Loading_List()
	print(len(listAll))
	if (len(text) == 3):
		for element in listAll:
			print(element)
			print(str.encode(text))
			valid=bcrypt.checkpw(str.encode(text), str.encode(element["Hash"]))
			
			if valid:
				print("Password Existing !" + element["Password"])
				Password = (element["Password"])
				result.config(text = "Password Existing !",fg='#fff',bg='Red')
				break
				
				

		if not valid:

			print("We didn't find the password With Hash please change the crypto Algorithm ")
			result.config(text = "Password Found not found")
			Password = ""
			result.config(text = "Password not Existing",fg='#fff',bg='#5BE62F')

	else :	
		print("We didn't find the password With Hash please change the crypto Algorithm ")
		result.config(text = "Password Found not found")
		Password = ""
		result.config(text = "Password not Existing",fg='#fff',bg='#5BE62F')



root =Tk()
root.title("Grinch")
root.iconphoto(False, PhotoImage(file='Grinch.png'))
root.configure(background='black')
root.geometry("750x500")
#-------------------------------------------------------------Labels-------------------------

main_Title  = Label(root, text = "Rainbow Table Attack", font =("Helvetica 20 bold underline"),fg='#fff',bg='#000').place(relx=.5, rely=.1,anchor= CENTER)
entry_Title = Label(root, text = "Type The Code",font =("Helvetica"),fg='#fff',bg='#000').place(relx=.5, rely=.3,anchor= CENTER)
result = Label(root, text = "",font =("Helvetica 35 bold"),fg='#fff',bg='#000')



button_border = Frame(root, highlightbackground = "white", 
                         highlightthickness = 2, bd=0)

button_border2 = Frame(root, highlightbackground = "white", 
                         highlightthickness = 2, bd=0)

#-------------------------------------------------------------Entries-------------------------
entry  = Entry(root,font =("Helvetica 20"))
entry.place(relx=.5, rely=.4,anchor= CENTER,  width = 500, height=40)
#-------------------------------------------------------------Buttons-------------------------
crack_it  = Button(button_border,text = "Crack IT",font= ('Helvetica 20 bold'), command =lambda: Cracking(entry.get()), fg='white',bg='black')
crack_it.pack()
match_it  = Button(button_border2,text = "Match IT",font= ('Helvetica 20 bold'), command =lambda: Matching(entry.get()), fg='white',bg='black')
match_it.pack()

button_border.place(relx=.65, rely=.55,anchor= CENTER)
button_border2.place(relx=.35, rely=.55,anchor= CENTER)


result.place(relx=.5, rely=.7,anchor= CENTER)








root.mainloop()