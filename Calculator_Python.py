from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Simple Calculator")

root.resizable(width=False, height=False)
root.iconbitmap("Calculator_Icon.ico")
inputs = Entry(root,width=15,borderwidth=5,font="Orbitron 20",justify="right")
inputs.grid(row=0,column=0,columnspan=5,ipadx=50,pady=5,ipady=30)

myfont=font.Font(size=15,weight="bold")


class calculator():

	def click(no):
		pno=inputs.get()
		inputs.delete(0,END)
		inputs.insert(0,str(pno)+str(no))
		res = inputs.get()
		print(res)	

	def clr():
		inputs.delete(0,END)
 	
	def equal():
		if (int(len(inputs.get()))) == 0 :return
			
		try:
			res=eval(inputs.get())
			inputs.delete(0,END)
			inputs.insert(0,res)
			
		except:
			print("Math Error")
			inputs.delete(0,END)
			inputs.insert(0,"Syntax Error")

	def one_back():
		inputs.delete(int(len(inputs.get())-1))	

#Numeric Buttons Specified
bt_7 = Button(root,text="7",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(7)).grid(row=1,column=0,sticky="nsew")
bt_8 = Button(root,text="8",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(8)).grid(row=1,column=1,sticky="nsew")
bt_9 = Button(root,text="9",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(9)).grid(row=1,column=2,sticky="nsew")
bt_4 = Button(root,text="4",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(4)).grid(row=2,column=0,sticky="nsew")
bt_5 = Button(root,text="5",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(5)).grid(row=2,column=1,sticky="nsew")
bt_6 = Button(root,text="6",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(6)).grid(row=2,column=2,sticky="nsew")
bt_1 = Button(root,text="1",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(1)).grid(row=3,column=0,sticky="nsew")
bt_2 = Button(root,text="2",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(2)).grid(row=3,column=1,sticky="nsew")
bt_3 = Button(root,text="3",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(3)).grid(row=3,column=2,sticky="nsew")
bt_0 = Button(root,text="0",padx=50,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(0)).grid(row=4,column=0,columnspan=2,sticky="nsew")
bt_dec = Button(root,text=".",padx=20,pady=1,bg="#808B96",fg="white",font=myfont,command=lambda: calculator.click(".")).grid(row=4,column=2,sticky="nsew")

#Operator's Buttons Specified
bt_add = Button(root,text="+",padx=20,pady=20,bg="#2ECC71",font=myfont,command=lambda: calculator.click("+")).grid(row=4,column=3,sticky="nsew")
bt_sub = Button(root,text="-",padx=20,pady=11,bg="#2ECC71",font=myfont,command=lambda: calculator.click("-")).grid(row=3,column=3,sticky="nsew")
bt_mul= Button(root,text="X",padx=20,pady=11,bg="#2ECC71",font=myfont,command=lambda: calculator.click("*")).grid(row=2,column=3,sticky="nsew")
bt_div = Button(root,text="/",padx=20,pady=11,bg="#2ECC71",font=myfont,command=lambda: calculator.click("/")).grid(row=1,column=3,sticky="nsew")
bt_sq = Button(root,text="x^",padx=20,pady=11,bg="#2ECC71",font=myfont,command=lambda: calculator.click("**")).grid(row=3,column=4,sticky="nsew")

#Resulting Buttons Specified
bt_clr = Button(root,text="AC",padx=15,pady=11,bg="orange",fg="black",font=myfont,command=calculator.clr).grid(row=2,column=4,sticky="nsew")
bt_equal_to = Button(root,text="=",padx=20,pady=11,bg="#3498DB",font=myfont,command=calculator.equal).grid(row=4,column=4,sticky="nsew")
bt_del = Button(root,text="DEL",padx=20,pady=10,bg="#CB4335",font=myfont,command=calculator.one_back).grid(row=1,column=4,sticky="nsew")

root.mainloop()
