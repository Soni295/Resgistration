from tkinter import *
from tkinter import ttk
import pickle


#--------------------------------------------Aplicacion-------------------------------------

Root=Tk()
Root.title("Registration")
Root.config(bg="#B6F0EB")
Root.resizable(0,0)
Root.geometry("400x500")

My_Frame=Frame(Root,width=400,height=500)
My_Frame.pack()


#------------------------------------------Class-----------------------------------------------


class People:

	List_Of_People=[]
	

	def __init__(self):

		Box=open("Data","ab+")
		Box.seek(0)

		try:		
			
			self.List_Of_People=pickle.load(Box)
			print("there are {} people registered".format(len(self.List_Of_People)))
	
		except:
			
			print("There is not person registered")
		
		finally:
			
			Box.close()

	def Watch(self,):
		for X in self.List_Of_People:
			print(X)

	def Add_People(self,p):
		
		self.List_Of_People.append(p)
		

	def Save(self):
		
		Box=open("Data","wb")
		pickle.dump(self.List_Of_People,Box)
		Box.close()

class Person:	
	

	def __init__(self,Name,Sur,Address,Email,Phone,Cell,District,Country):
		
		self.Name=Name
		self.Sur=Sur
		self.Address=Address
		self.Email=Email
		self.Phone=Phone
		self.Cell=Cell
		self.District=District
		self.Country=Country
	

	def __str__(self):

		return ("{}, {}, {}, {}, {}, {}, {}, {}".format(self.Name,self.Sur,self.Address
			,self.Email,self.Phone,self.Cell,self.District,self.Country))


#------------------------------------------Funtions--------------------------------------------

def Send_Data():

	global User

	User=Person(Name_Text.get(),Last_Name_Text.get(),Address_Text.get(),Email_Text.get()
	,Phone_Text.get(),Cell_Text.get(),District_Text.get(),Country_Text.get())

	My_list.Add_People(User)

	My_list.Watch()
	My_list.Save()
	

#--------------------------------------------Variable-------------------------------------------


ID=0
Name_Text=StringVar()
Last_Name_Text=StringVar()
Address_Text=StringVar()
Email_Text=StringVar()
Phone_Text=StringVar()
Cell_Text=StringVar()
District_Text=StringVar()
Country_Text=StringVar()

User=""
My_list=People()


#--------------------------------------------Data------------------------------------------------


Information=Label(My_Frame, text="Information")
Information.grid(row=0,column=0,padx=5,pady=5,columnspan=2,sticky="nsew")
Information.config(bg="#B6F0EB",font=("times new roman", 30))

Name=Label(My_Frame, text="Name:")
Name.grid(row=1,column=0,padx=5,pady=5,sticky="e")
Name.config(bg="#B6F0EB",font=("times new roman", 18))

Last_Name=Label(My_Frame, text="Last Name:")
Last_Name.grid(row=2,column=0,padx=5,pady=5,sticky="e")
Last_Name.config(bg="#B6F0EB",font=("times new roman", 18))

Address=Label(My_Frame, text="Address:")
Address.grid(row=3,column=0,padx=5,pady=5,sticky="e")
Address.config(bg="#B6F0EB",font=("times new roman", 18))

Email=Label(My_Frame, text="E-Mail:")
Email.grid(row=4,column=0,padx=5,pady=5,sticky="e")
Email.config(bg="#B6F0EB",font=("times new roman", 18))

Phone=Label(My_Frame, text="Phone:")
Phone.grid(row=5,column=0,padx=5,pady=5,sticky="e")
Phone.config(bg="#B6F0EB",font=("times new roman", 18))

Cell_Phone=Label(My_Frame, text="Cell Phone:")
Cell_Phone.grid(row=6,column=0,padx=5,pady=5,sticky="e")
Cell_Phone.config(bg="#B6F0EB",font=("times new roman", 18))

District=Label(My_Frame, text="District:")
District.grid(row=7,column=0,padx=5,pady=5,sticky="e")
District.config(bg="#B6F0EB",font=("times new roman", 18))

Country=Label(My_Frame, text="Country:")
Country.grid(row=8,column=0,padx=5,pady=5,sticky="e")
Country.config(bg="#B6F0EB",font=("times new roman", 18))


#------------------------------------------------text-------------------------------------------------


Text0=Entry(My_Frame,textvariable=Name_Text)
Text0.grid(row=1,column=1,padx=5,pady=5)
Text0.config(font=("times new roman", 16))
Text0.focus()

Text1=Entry(My_Frame,textvariable=Last_Name_Text)
Text1.grid(row=2,column=1,padx=5,pady=5)
Text1.config(font=("times new roman", 16))

Text2=Entry(My_Frame,textvariable=Address_Text)
Text2.grid(row=3,column=1,padx=5,pady=5)
Text2.config(font=("times new roman", 16))

Text3=Entry(My_Frame,textvariable=Email_Text)
Text3.grid(row=4,column=1,padx=5,pady=5)
Text3.config(font=("times new roman", 16))

Text4=Entry(My_Frame,textvariable=Phone_Text)
Text4.grid(row=5,column=1,padx=5,pady=5)
Text4.config(font=("times new roman", 16))

Text5=Entry(My_Frame,textvariable=Cell_Text)
Text5.grid(row=6,column=1,padx=5,pady=5)
Text5.config(font=("times new roman", 16))

Text6=Entry(My_Frame,textvariable=District_Text)
Text6.grid(row=7,column=1,padx=5,pady=5)
Text6.config(font=("times new roman", 16))

Text7=Entry(My_Frame,textvariable=Country_Text)
Text7.grid(row=8,column=1,padx=5,pady=5)
Text7.config(font=("times new roman", 16))
My_Frame.config(bg="#B6F0EB")
#------------------------------------------------Button---------------------------------------


Send=Button(My_Frame,text="Send",command=Send_Data,width=8,height=2)
Send.grid(row=9,column=1,padx=5,pady=5)
Send.config(font=("times new roman", 12))

My_Frame.config(bg="#B6F0EB")

Root.mainloop()